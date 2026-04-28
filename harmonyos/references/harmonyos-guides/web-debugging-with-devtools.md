---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-debugging-with-devtools
title: 使用DevTools工具调试前端页面
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > Web调试维测 > 使用DevTools工具调试前端页面
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:10e9b6615802a32118cb12f2cb3caf43397cd439b138cd5a717e6aab73492607
---

Web组件支持使用DevTools工具调试前端页面。DevTools是Web前端开发调试工具，支持在电脑上调试移动设备前端页面。开发者通过[setWebDebuggingAccess()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess)接口开启Web组件前端页面调试能力，使用DevTools在电脑上调试移动前端网页，设备需为4.1.0及以上版本。

## 无线调试

从API version 20开始，可使用无线调试接口[setWebDebuggingAccess20+](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess20)，来简化调试流程。

### 应用代码开启Web调试开关

调试网页前，需要应用侧代码调用setWebDebuggingAccess()接口开启Web调试开关。

如果没有开启Web调试开关，则DevTools无法发现被调试的网页。

1. 在应用代码中开启Web调试开关，应用需要调用[setWebDebuggingAccess20+](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess20)接口，设置TCP Socket端口号并启用Web调试功能。

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. const DEBUGGING_PORT: number = 8888;

   5. @Entry
   6. @Component
   7. struct WebComponent {
   8. controller: webview.WebviewController = new webview.WebviewController();

   10. aboutToAppear(): void {
   11. try {
   12. // 配置Web开启无线调试模式，指定TCP Socket的端口。
   13. webview.WebviewController.setWebDebuggingAccess(true, DEBUGGING_PORT);
   14. } catch (error) {
   15. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
   16. }
   17. }

   19. build() {
   20. Column() {
   21. Web({ src: 'www.example.com', controller: this.controller })
   22. }
   23. }
   24. }
   ```

   [WebDebuggingWithWiFi.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebDebuggingWithDevtools/entry/src/main/ets/pages/WebDebuggingWithWiFi.ets#L15-L40)

   说明

   代码中使用的8888端口仅作为示例展示，开发者使用过程中，应保证端口号可以被应用使用。如果因为端口被占用或者应用无权限使用等因素导致端口无法被应用使用，会导致接口抛出异常或者ArkWeb无法开启调试模式。
2. 开启调试功能需要在DevEco Studio应用工程hap模块的module.json5文件中增加如下权限，添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

   ```
   1. "requestPermissions":[
   2. {
   3. "name" : "ohos.permission.INTERNET"
   4. }
   5. ]
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebDebuggingWithDevtools/entry/src/main/module.json5#L63-L69)

### 在Chrome浏览器上打开调试工具页面

1. 在电脑端Chrome浏览器地址栏中输入调试工具地址 chrome://inspect/#devices 并打开该页面。
2. 修改Chrome调试工具的配置。

   确保已勾选 "Discover network targets"，以便从指定的IP地址和端口号发现被调试网页。

   (1) 点击 "Configure" 按钮。

   (2) 在 "Target discovery settings" 中添加被调试设备的IP地址和[setWebDebuggingAccess20+](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess20)接口中指定的port端口，比如：192.168.0.3:8888。

说明

调试工具和被调试设备要在同一局域网下，并且能够相互访问。如果被调试设备有多个IP地址，要使用与调试工具同一个网段的IP地址。

### 等待发现被调试页面

如果前面的步骤执行成功，Chrome的调试页面将显示待调试的网页。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/NLAhelKuSMe50gxIMc8J9w/zh-cn_image_0000002583478249.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=C6D936323B184BA70304EE3B8806713D0D541B18687F15FB896845CCD83918BE)

### 开始网页调试

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/upJ7z_AfTBOmIt4xeqTdgw/zh-cn_image_0000002552798600.png?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=168A81B81893086885772E57FA8B9117D18A8C7F66FC95FBDAD2870C8B01873A)

## USB连接调试

### 应用代码开启Web调试开关

调试网页前，需要应用侧代码调用[setWebDebuggingAccess()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess)接口开启Web调试开关。

如果没有开启Web调试开关，则DevTools无法发现被调试的网页。

1. 在应用代码中开启Web调试开关，具体如下：

   ```
   1. import { webview } from '@kit.ArkWeb';

   3. @Entry
   4. @Component
   5. struct WebComponent {
   6. controller: webview.WebviewController = new webview.WebviewController();

   8. aboutToAppear() {
   9. // 配置Web开启调试模式
   10. webview.WebviewController.setWebDebuggingAccess(true);
   11. }

   13. build() {
   14. Column() {
   15. Web({ src: 'www.example.com', controller: this.controller })
   16. }
   17. }
   18. }
   ```

   [WebDebuggingWithUSB.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebDebuggingWithDevtools/entry/src/main/ets/pages/WebDebuggingWithUSB.ets#L15-L34)
2. 开启调试功能需要在DevEco Studio应用工程hap模块的module.json5文件中增加如下权限，添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

   ```
   1. "requestPermissions":[
   2. {
   3. "name" : "ohos.permission.INTERNET"
   4. }
   5. ]
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebDebuggingWithDevtools/entry/src/main/module.json5#L63-L69)

### 将设备连接至电脑

请将设备连接至电脑，随后开启开发者模式，为后续的端口转发操作做好准备。

1. 请开启设备上的开发者模式，并启用USB调试功能。

   (1) 终端系统查看“设置 > 系统”中是否有“开发者选项”，如果不存在，可在“设置 > 关于本机”连续七次单击“版本号”，直到提示“开启开发者模式”，点击“确认开启”后输入PIN码（如果已设置），设备将自动重启。

   (2) USB数据线连接终端和电脑，在“设置 > 系统 > 开发者选项”中，打开“USB调试”开关，弹出的“允许USB调试”的弹框，点击“允许”。
2. 使用hdc命令连接上设备。

   打开命令行执行如下命令，查看hdc能否发现设备。

   ```
   1. hdc list targets
   ```

   * 如果命令返回设备的ID，表示hdc已连接上设备。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/eaCYOk48RPOTr7rl2bkvNw/zh-cn_image_0000002583438295.png?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=7CB4BBC491FF1F057116DDE661418CA744627D7CEBACB30A3D3E666727EAF0BA)
   * 如果命令返回 [Empty]，则说明hdc还没有发现设备。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/0MLsW-HzSNeD3L-HuV_vqQ/zh-cn_image_0000002552958250.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=8AF8DB3EB28DA83217D1C0AD5BA9C96F81793C1112B7DDEA8B32C4D649AEB710)
3. 进入hdc shell。

   连接设备后，执行以下命令进入hdc shell。

   ```
   1. hdc shell
   ```

### 端口转发

当应用代码调用setWebDebuggingAccess接口开启Web调试开关后，ArkWeb内核将启动一个domain socket的监听，以此实现DevTools对网页的调试功能。

Chrome浏览器无法直接访问到设备上的domain socket， 因此需要将设备上的domain socket转发到电脑上。

**推荐使用[自动映射WebView调试链接](ide-run-debug-configurations.md#section48387420516)**。

若当前DevEco版本低，可参考以下方法：

1. 先在hdc shell里执行如下命令，查询ArkWeb在设备里创建的domain socket。

   ```
   1. cat /proc/net/unix | grep devtools
   ```

   * 如果前几步操作无误，该命令的执行结果将显示用于查询的domain socket端口。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/dgPiGkgiT6--AQMafkjhzg/zh-cn_image_0000002583478251.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=45895D40BBA12B0527DF9D7A40BFB5CD949621263DC748C26FF2E123C1E80FFA)
   * 如果没有查询到结果， 请再次确认。

     (1) 应用开启了Web调试开关。

     (2) 应用使用Web组件加载了网页。
2. 将查询到的domain socket转发至电脑的TCP 9222端口。

   执行exit退出hdc shell。

   ```
   1. exit
   ```

   在命令行里执行如下命令转发端口。

   ```
   1. hdc fport tcp:9222 localabstract:webview_devtools_remote_38532
   ```

   说明

   "webview\_devtools\_remote\_" 后面的数字，代表ArkWeb所在应用的进程号， 该数字不是固定的。请将”webview\_devtools\_remote\_“后面的数字改为自己查询到的值。

   如果应用的进程号发生变化，例如，应用重新启动，则需要重新配置端口转发。

   命令执行成功示意图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ruRh6ezGRLOa2M-WU5CF6A/zh-cn_image_0000002552798602.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=9A5A6C46B7F53AA5F4EE288CDE396470C7CB304DE952542DB4525D5AC3525AE2)
3. 在命令行里执行如下命令，检查端口是否转发成功。

   ```
   1. hdc fport ls
   ```

   * 如果有返回端口转发的任务，则说明端口转发成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/2hLmjDQWRlum3KTJdDTG0w/zh-cn_image_0000002583438297.png?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=8C7D7A4C250F9B7C055E7C172AA18D9F0E1C95C83B1690007AE314B9E76B2798)
   * 如果返回 [Empty]， 则说明端口转发失败。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/jfpTlV3WTzeFIb37Nhlytg/zh-cn_image_0000002552958252.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=C798E84B91D1AB3F07CB83BA5D8409381F9036710AB1E2F6A2D5D4F7532D7F2F)

### 便捷脚本

**Windows平台**

请复制以下信息创建bat文件，开启调试应用后执行。

```
1. @echo off
2. setlocal enabledelayedexpansion

4. :: Initialize port number and PID list
5. set PORT=9222
6. set PID_LIST=

8. :: Get the list of all forwarded ports and PIDs
9. for /f "tokens=2,5 delims=:_" %%a in ('hdc fport ls') do (
10. if %%a gtr !PORT! (
11. set PORT=%%a
12. )
13. for /f "tokens=1 delims= " %%c in ("%%b") do (
14. set PID_LIST=!PID_LIST! %%c
15. )
16. )

18. :: Increment port number for next application
19. set temp_PORT=!PORT!
20. set /a temp_PORT+=1
21. set PORT=!temp_PORT!

23. :: Get the domain socket name of devtools
24. for /f "tokens=*" %%a in ('hdc shell "cat /proc/net/unix | grep devtools"') do (
25. set SOCKET_NAME=%%a

27. :: Extract process ID
28. for /f "delims=_ tokens=4" %%b in ("!SOCKET_NAME!") do set PID=%%b

30. :: Check if PID already has a mapping
31. echo !PID_LIST! | findstr /C:" !PID! " >nul
32. if errorlevel 1 (
33. :: Add mapping
34. hdc fport tcp:!PORT! localabstract:webview_devtools_remote_!PID!
35. if errorlevel 1 (
36. echo Error: Failed to add mapping.
37. pause
38. exit /b
39. )

41. :: Add PID to list and increment port number for next application
42. set PID_LIST=!PID_LIST! !PID!
43. set temp_PORT=!PORT!
44. set /a temp_PORT+=1
45. set PORT=!temp_PORT!
46. )
47. )

49. :: If no process ID was found, prompt the user to open debugging in their application code and provide the documentation link
50. if "!SOCKET_NAME!"=="" (
51. echo No process ID was found. Please open debugging in your application code using the corresponding interface. You can find the relevant documentation at this link: [https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/web/web-debugging-with-devtools.md]
52. pause
53. exit /b
54. )

56. :: Check mapping
57. hdc fport ls

59. echo.
60. echo Script executed successfully. Press any key to exit...
61. pause >nul

63. :: Try to open the page in Edge
64. start msedge chrome://inspect/#devices

66. :: If Edge is not available, then open the page in Chrome
67. if errorlevel 1 (
68. start chrome chrome://inspect/#devices
69. )

71. endlocal
```

**Linux或Mac平台**

请复制以下信息创建sh文件，注意chmod以及格式转换，开启调试应用后执行。

本脚本会先删除所有的端口转发，如果有其他的工具（如：DevEco Studio）也在使用端口转发功能，会受到影响。

```
1. #!/bin/bash

3. # Get current fport rule list
4. CURRENT_FPORT_LIST=$(hdc fport ls)

6. # Delete the existing fport rule one by one
7. while IFS= read -r line; do
8. # Extract the taskline
9. IFS=' ' read -ra parts <<< "$line"
10. taskline="${parts[1]} ${parts[2]}"

12. # Delete the corresponding fport rule
13. echo "Removing forward rule for $taskline"
14. hdc fport rm $taskline
15. result=$?

17. if [ $result -eq 0 ]; then
18. echo "Remove forward rule success, taskline:$taskline"
19. else
20. echo "Failed to remove forward rule, taskline:$taskline"
21. fi

23. done <<< "$CURRENT_FPORT_LIST"

25. # Initial port number
26. INITIAL_PORT=9222

28. # Get the current port number, use initial port number if not set previously
29. CURRENT_PORT=${PORT:-$INITIAL_PORT}

31. # Get the list of all PIDs that match the condition
32. PID_LIST=$(hdc shell cat /proc/net/unix | grep webview_devtools_remote_ | awk -F '_' '{print $NF}')

34. if [ -z "$PID_LIST" ]; then
35. echo "Failed to retrieve PID from the device"
36. exit 1
37. fi

39. # Increment the port number
40. PORT=$CURRENT_PORT

42. # Forward ports for each application one by one
43. for PID in $PID_LIST; do
44. # Increment the port number
45. PORT=$((PORT + 1))

47. # Execute the hdc fport command
48. hdc fport tcp:$PORT localabstract:webview_devtools_remote_$PID

50. # Check if the command executed successfully
51. if [ $? -ne 0 ]; then
52. echo "Failed to execute hdc fport command"
53. exit 1
54. fi
55. done

57. # List all forwarded ports
58. hdc fport ls
```

### 在Chrome浏览器上打开调试工具页面

1. 在电脑端Chrome浏览器地址栏中输入调试工具地址 chrome://inspect/#devices 并打开该页面。
2. 修改Chrome调试工具的配置。

   需要从本地的TCP 9222端口发现被调试网页，所以请确保已勾选 "Discover network targets"。然后再进行网络配置。

   (1) 点击 "Configure" 按钮。

   (2) 在 "Target discovery settings" 中添加要监听的本地端口localhost:9222。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/UygwNeodRt-4-29xfONngw/zh-cn_image_0000002583478253.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=2497D2BB8BCA8791E396BB7A31004E4918D053FCCEC8D9A9A03F80620481C527)
3. 为了同时调试多个应用，请在Chrome浏览器的调试工具网页内，于“Devices”选项中的“configure”部分添加多个端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/4vwwVdaGRGuSC5Kjv0_1ZA/zh-cn_image_0000002552798604.png?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=BCA85125B0CAF8314E0B1E4F4F30C485C029E3BF688190BBB5D99AFF5375A59F)

### 等待发现被调试页面

如果前面的步骤执行成功，Chrome的调试页面将显示待调试的网页。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/lvI5096zSQ6hsxBIsg7cPQ/zh-cn_image_0000002583478249.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=18F61A206BA9D4DC5D50D746D1F1D420AEC1E56BCFE2E4B259AFA1C4FB4803BC)

### 开始网页调试

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/bx7p-FRlQJulRtKIZI7uug/zh-cn_image_0000002552798600.png?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=DB5C5E6BD7A7EF760126371A26379B3BB46F2FEF34CE5DA75BC2213CBD1EBEF4)

## 常见问题与解决方法

### 可以调试系统浏览器打开的网页吗？

能否调试系统浏览器打开的网页，取决于系统浏览器是否开启Web调试开关。

* 当前系统浏览器已启用Web调试开关，可继续执行[USB连接调试](web-debugging-with-devtools.md#usb连接调试)中的后续步骤。

### hdc无法发现设备

**问题现象**

在命令行里执行如下命令后，没有列出设备ID。

```
1. hdc list targets
```

**解决方法**

* 请确保设备上的USB调试开关已开启。
* 请确保设备与电脑相连。

### hdc的命令显示设备"未授权"或"unauthorized"

**问题现象**

执行hdc命令时，提示设备"未授权"或"unauthorized"。

**问题原因**

设备没有授权该台电脑进行调试。

**解决方法**

开启USB调试开关的设备连接没有授权的电脑后，会弹框提示"是否允许USB调试？"，请选择允许。

### 找不到DevTools的domain socket

**问题现象**

1. 在hdc shell里执行如下命令后，没有结果。

   ```
   1. cat /proc/net/unix | grep devtools
   ```
2. 运行脚本出现'Failed to retrieve PID from the device'报错。

**解决方法**

* 请确保应用[开启了Web调试开关](web-debugging-with-devtools.md#应用代码开启web调试开关)。
* 请确保应用使用Web组件加载了网页。

### 删除端口转发任务失败

**问题现象**

运行脚本出现'Failed to remove forward rule, taskline:'报错。

**解决方法**

* 执行hdc kill终止hdc服务，再执行hdc start重启服务。
* 执行hdc list targets确认设备在线状态，若返回空则重新连接设备。

### 端口转发不成功

**问题现象**

1. 在命令行里执行如下命令后，没有列出之前设置过转发任务。

   ```
   1. hdc fport ls
   ```
2. 运行脚本出现'Failed to execute hdc fport command'报错。

**解决方法**

* 请确保设备里的domain socket存在。
* 请确保电脑端的tcp:9222没有被占用。

  如果tcp:9222被占用，可以将domain socket转发到其他未被占用的TCP端口， 比如9223等。

  如果转发到了新的TCP端口， 需要同步修改电脑端Chrome浏览器"Target discovery settings"中的端口号。

### 端口转发成功后，电脑端Chrome无法发现被调试网页

**问题现象**

电脑端Chrome浏览器无法发现被调试网页。

**问题原因**

端口转发失效可能是以下原因：

* 设备与电脑断连，会导致hdc里的所有转发任务被清空。
* hdc服务重启，也会导致hdc里的所有转发任务被清空。
* 设备里应用的进程号发生了变更（应用重新启动等），会导致hdc里旧的转发任务失效。
* 多个转发任务转发到了同一个端口等异常配置，会导致转发异常。

**解决方法**

* 请确保电脑端的本地tcp:9222（其他TCP端口同理）没有被占用。
* 请确保设备端的domain socket还存在。
* 请确保domain socket名称里的进程号与被调试的应用的进程号相同。
* 请删除hdc里其他不必要的转发任务。
* 转发成功后，请用电脑端的Chrome浏览器打开网址 <http://localhost:9222/json> ，URL里的9222需要改为自己实际配置的TCP端口。

  + 如果网页有内容， 说明端口转发成功，请在Chrome的调试页面[等待被调试页面的出现](web-debugging-with-devtools.md#等待发现被调试页面)。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/obi0-GYpRdyMN7zow6kdjw/zh-cn_image_0000002583438299.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=54D40C1AD6EFBB4115D7C5752850A1E03B9BB1B64B95967D1F9379FCA6DE4202)
  + 如果展示的是错误网页， 说明端口转发失败， 请参阅[端口转发不成功](web-debugging-with-devtools.md#端口转发不成功)中的解决方法。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/ab_sf_krR2qfQlY8DW0utQ/zh-cn_image_0000002552958254.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234106Z&HW-CC-Expire=86400&HW-CC-Sign=EB550C6BA5842ECD4FEC72E825EB68517001A32CB6E0E94AB6C588A10F41D6B1)
* 电脑端Chrome浏览器打开 <http://localhost:9222/json> 页面有内容，但是Chrome的调试工具界面还是无法发现调试目标。

  + 请确保Chrome调试工具界面的 "Configure" 中配置的端口号，与端口转发指定的TCP端口号一致。
  + 在本文档中，默认使用的TCP端口号为9222。

    如果开发者使用了其他的TCP端口号（比如9223），请同时修改[端口转发](web-debugging-with-devtools.md#端口转发)中的TCP端口号和[Chrome调试工具界面"Configure"配置](web-debugging-with-devtools.md#在chrome浏览器上打开调试工具页面)中的端口号。

### 开启了无线调试模式后，电脑端Chrome无法发现被调试网页

**问题现象**

ArkWeb开启了无线调试模式后，电脑端Chrome浏览器无法发现被调试网页。

**问题原因**

* 无线调试模式没有成功开启。
* 调试工具和被调试设备之间网络不通。

**解决方法**

* 请确保使用的端口可以被应用使用。
* 请确保调试工具和被调试设备在同一个局域网内，且它们之间网络通畅。

### Web组件无法使用DevTools工具进行调试

**问题现象**

电脑端Chrome浏览器无法发现被调试网页。

**问题原因**

* 当同时使用HDC和ADB时，ADB会干扰DevTools与设备之间的WebSocket连接。

**解决方法**

* 如果同时使用HDC和ADB，先关闭ADB进程，确保DevTools与设备建立WebSocket连接。

### 使用DevTools工具进行调试出现404报错

**问题现象**

在电脑端Chrome浏览器中调试网页时，出现报错：“HTTP/1.1 404 Not Found”。

**问题原因**

* Chrome浏览器版本较低，导致无法使用DevTools调试。

**解决方法**

* 方案一，将电脑端Chrome升级到最新版本。
* 方案二，如果不希望升级浏览器，可以手动拼接调试URL。完整的URL链接为：“devtools://devtools/bundled/inspector.html?ws=localhost:9222/devtools/page/xxx”。
  + 该链接由两部分组成：“devtools://devtools/bundled/inspector.html”前半段固定不变。“?ws=localhost:9222/devtools/page/xxx”后半段需要根据实际配置修改。
  + 端口转发成功后，使用Chrome浏览器打开 <http://localhost:9222/json> 页面。请注意，URL中的9222应替换为实际配置的TCP端口。然后取“devtoolsFrontendUrl”后的value值“?ws”及其后部分。
