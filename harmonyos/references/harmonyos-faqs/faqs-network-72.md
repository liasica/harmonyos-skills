---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-72
title: 多种网络同时连接时如何优先使用wifi网络
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 多种网络同时连接时如何优先使用wifi网络
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7e307368a3129f8cd18ad4fdb6fd2db0722b4fdc14b3bca74f6aae66e1a03daf
---

**问题现象**

使用video组件加载网络视频，发现使用蓝牙网络时视频加载较慢，而WiFi网络较快，需要优先使用WiFi网络。

**解决措施**

1. 申请权限ohos.permission.INTERNET,ohos.permission.GET\_NETWORK\_INFO。Stage模型中，在module.json5配置文件中声明权限：

   ```
   1. {
   2. "module": {
   3. // ...
   4. "requestPermissions":[
   5. {
   6. "name": "ohos.permission.INTERNET",
   7. "reason": "$string:internet_reason",
   8. "usedScene": {
   9. "abilities": [
   10. "EntryAbility"
   11. ],
   12. "when": "inuse"
   13. }
   14. },
   15. {
   16. "name" : "ohos.permission.GET_NETWORK_INFO",
   17. "reason": "$string:internet_reason",
   18. "usedScene": {
   19. "abilities": [
   20. "EntryAbility"
   21. ],
   22. "when":"inuse"
   23. }
   24. },
   25. ]
   26. }
   27. }
   ```

   [module\_getNetwork.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/9599520cea2cd471e1e3ed244c5fc384697af3e6/NetworkKit/entry/src/main/module_getNetwork.json5#L2-L77)
2. 编写优先使用wifi网络管理类。

   ```
   1. // WifiManager.ets
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { connection } from '@kit.NetworkKit';

   5. export class WifiManager {
   6. private static instance?: WifiManager;

   8. /**
   9. * Get singleton
   10. *
   11. * @returns Singleton object
   12. */
   13. public static getInstance(): WifiManager {
   14. if (!WifiManager.instance) {
   15. WifiManager.instance = new WifiManager();
   16. }
   17. return WifiManager.instance;
   18. }

   20. /**
   21. * Start listening for network changes (Wi-Fi network / Bluetooth network / cellular data)
   22. */
   23. public startListenNetChange(): void {
   24. console.info("registerNetListener");
   25. let netConnectionWifi = connection.createNetConnection({
   26. netCapabilities: {
   27. bearerTypes: [connection.NetBearType.BEARER_WIFI]
   28. }
   29. });
   30. netConnectionWifi.register((error: BusinessError) => {
   31. if (error) {
   32. console.error(`register error: ${error.code}`);
   33. }
   34. });
   35. netConnectionWifi.on('netAvailable', () => {
   36. console.info("netConnectionWifi netAvailable");
   37. this.bindWifiWhenConnected();
   38. });
   39. netConnectionWifi.on('netLost', () => {
   40. console.info("Wifi netLost");
   41. this.bindWifiWhenConnected();
   42. });
   43. let netConnectionBluetooth = connection.createNetConnection({
   44. netCapabilities: {
   45. bearerTypes: [connection.NetBearType.BEARER_BLUETOOTH]
   46. }
   47. });
   48. netConnectionBluetooth.register((error: BusinessError) => {
   49. if (error) {
   50. console.error(`register error: ${error.code}`);
   51. }
   52. });
   53. netConnectionBluetooth.on('netAvailable', () => {
   54. console.info('netConnectionBluetooth netAvailable');
   55. this.bindWifiWhenConnected();
   56. });
   57. netConnectionBluetooth.on('netLost', () => {
   58. console.info('Bluetooth netLost');
   59. this.bindWifiWhenConnected();
   60. });
   61. let netConnectionCellular = connection.createNetConnection({
   62. netCapabilities: {
   63. bearerTypes: [connection.NetBearType.BEARER_CELLULAR]
   64. }
   65. });
   66. netConnectionCellular.register((error: BusinessError) => {
   67. if (error) {
   68. console.error(`register error: ${error.message}`);
   69. }
   70. });
   71. netConnectionCellular.on('netAvailable', () => {
   72. console.info('netConnectionCellular netAvailable');
   73. this.bindWifiWhenConnected();
   74. });
   75. netConnectionCellular.on('netLost', () => {
   76. console.info('Cellular netLost');
   77. this.bindWifiWhenConnected();
   78. });
   79. }

   81. /**
   82. * Connect the App to the Wi-Fi network asynchronously
   83. */
   84. private async bindWifiWhenConnected(): Promise<void> {
   85. await connection.setAppNet(connection.getDefaultNetSync()).then(() => {
   86. console.info('setAppNet default success')
   87. });
   88. connection.getAllNets().then((data: connection.NetHandle[]) => {
   89. data.forEach(net => {
   90. connection.getNetCapabilities(net).then((data: connection.NetCapabilities) => {
   91. if (data.bearerTypes.length > 0 && data.bearerTypes[0] === connection.NetBearType.BEARER_WIFI) {
   92. connection.setAppNet(net).then(() => {
   93. console.info('setAppNet wifi success');
   94. return;
   95. }).catch((error: Error) => {
   96. console.error(`setAppNet wifi failed, error = ${error.message}`);
   97. })
   98. }
   99. }).catch((error: Error) => {
   100. console.error(`getNetCapabilities error = ${error.message}`);
   101. });
   102. })
   103. }).catch((error: Error) => {
   104. console.error(`getAllNets error = ${error.message}`);
   105. });
   106. }
   107. }
   ```

   [WifiManager.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/9599520cea2cd471e1e3ed244c5fc384697af3e6/NetworkKit/entry/src/main/ets/pages/WifiManager.ets#L21-L127)
3. 获取实例并调用监听方法。

   ```
   1. import { WifiManager } from './WifiManager'

   3. // Register for change monitoring
   4. WifiManager.getInstance().startListenNetChange();
   ```

   [StartListenNetChange.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/9599520cea2cd471e1e3ed244c5fc384697af3e6/NetworkKit/entry/src/main/ets/pages/StartListenNetChange.ets#L21-L24)

**参考链接**

[connection.createNetConnection](../harmonyos-references/js-apis-net-connection.md#connectioncreatenetconnection)

[connection.setAppNet](../harmonyos-references/js-apis-net-connection.md#connectionsetappnet9-1)

[connection.getAllNets](../harmonyos-references/js-apis-net-connection.md#connectiongetallnets-1)

[connection.getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities-1)
