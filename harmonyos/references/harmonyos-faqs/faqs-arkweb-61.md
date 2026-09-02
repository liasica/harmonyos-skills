---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-61
title: 如何解决webview每次调试都需要寻找进程号问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决webview每次调试都需要寻找进程号问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5512ec09f2ccaff47d86dc9ff682368531939664fdcfed8abe9f2866bbcdba6e
---

**问题背景：**

在应用开发过程中，调试Web页面时，每次启动DevTools都需要重新映射端口。

**解决方案：**

参考以下示例代码，文件内容编写完成后，将文件扩展名更改为.bat。每次调试后，运行bat文件以自动获取进程号。

```ts
// xxx.bat
@echo off
setlocal

:: Set devtools parameter
hdc shell param set web.debug.devtools true
if errorlevel 1 (
    echo Error: Failed to set devtools parameter.
    pause
    exit /b
)

:: Get the domain socket name of devtools
for /f "tokens=*" %%a in ('hdc shell "cat /proc/net/unix | grep devtools"') do set SOCKET_NAME=%%a
if not defined SOCKET_NAME (
    echo Error: Failed to get the domain socket name of devtools.
    pause
    exit /b
)

:: Extract process ID
// tokens=4 indicates extracting the field separated by the fourth underscore as the PID
for /f "delims=_ tokens=4" %%a in ("%SOCKET_NAME%") do set PID=%%a
if not defined PID (
    echo Error: Failed to extract process ID.
    pause
    exit /b
)

:: Add mapping
hdc fport tcp:9222 localabstract:webview_devtools_remote_%PID%
if errorlevel 1 (
    echo Error: Failed to add mapping.
    pause
    exit /b
)

:: Check mapping
hdc fport ls

echo.
echo Script executed successfully. Press any key to exit...
pause >nul

:: Try opening the page in Edge
start msedge chrome://inspect/#devices.com

:: If Edge is unavailable, open the page in Chrome
if errorlevel 1 (
    start chrome chrome://inspect/#devices.com
)

endlocal
```
