import win32api as winapi

try: 
	print(winapi.GetCommandLine(" REG ADD HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\Albert"))
	print(winapi.GetCommandLine("REG ADD HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce /v Albert /t REG_MULTI_SZ /f"))
except Exception as e:
	error = str(e)
	print(error)
