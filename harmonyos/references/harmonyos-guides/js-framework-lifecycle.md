---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-lifecycle
title: 生命周期
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 框架说明 > 生命周期
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ca62e66095eeeed2b45edd0cf74edbbc2bb5dc2f9eb923250ec6174569d77214
---

## 应用生命周期

在app.js中可以定义如下应用生命周期函数：

| 属性 | 类型 | 描述 | 触发时机 |
| --- | --- | --- | --- |
| onCreate | () => void | 应用创建 | 当应用创建时调用。 |
| onShow6+ | () => void | 应用处于前台 | 当应用处于前台时触发。 |
| onHide6+ | () => void | 应用处于后台 | 当应用处于后台时触发。 |
| onDestroy | () => void | 应用销毁 | 当应用退出时触发。 |

## 页面生命周期

在页面JS文件中可以定义如下页面生命周期函数：

| 属性 | 类型 | 描述 | 触发时机 |
| --- | --- | --- | --- |
| onInit | () => void | 页面初始化 | 页面数据初始化完成时触发，只触发一次。 |
| onReady | () => void | 页面创建完成 | 页面创建完成时触发，只触发一次。 |
| onShow | () => void | 页面显示 | 页面显示时触发。 |
| onHide | () => void | 页面消失 | 页面消失时触发。 |
| onDestroy | () => void | 页面销毁 | 页面销毁时触发。 |
| onBackPress | () => boolean | 返回按钮动作 | 当用户点击返回按钮时触发。  - 返回true表示页面自己处理返回逻辑。  - 返回false表示使用默认的返回逻辑。  - 不返回值会作为false处理。 |
| onActive()5+ | () => void | 页面激活 | 页面激活时触发。 |
| onInactive()5+ | () => void | 页面暂停 | 页面暂停时触发。 |
| onNewRequest()5+ | () => void | FA重新请求 | FA已经启动时收到新的请求后触发。 |

生命周期函数的一般调用顺序如下所示：

**图1** 生命周期函数调用顺序图示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/elkibFFCQSyNhmrkk47w3A/zh-cn_image_0000002589244379.png?HW-CC-KV=V1&HW-CC-Date=20260429T052840Z&HW-CC-Expire=86400&HW-CC-Sign=9A91513FC8D7CD2CD13B51AA20CCD2EEC741A0205054E5933D20F10ADF5B7616)

## 示例代码

通过以下示例，详细说明生命周期函数的调用顺序。首先创建两个页面，分别为pageA和pageB，并在config.json中配置页面路由信息：

```
1. {
2. // ...
3. "pages": [
4. "pages/pageA/pageA",
5. "pages/pageB/pageB"
6. ],
7. // ...
8. }
```

pageA实现代码如下：

```
1. <!-- pageA.hml -->
2. <div class="container">
3. <text class="title">This is PageA</text>
4. <input type="button" value="Go to the PageB" onclick="launch"></input>
5. </div>
```

```
1. /* pageA.css */
2. .container {
3. flex-direction: column;
4. align-items: center;
5. width: 100%;
6. height: 100%;
7. }
8. .title {
9. font-size: 38px;
10. text-align: center;
11. width: 100%;
12. height: 40%;
13. }
```

```
1. // pageA.js
2. import router from '@ohos.router';
3. export default {
4. launch() {
5. router.push ({
6. url: 'pages/pageB/pageB'
7. });
8. },
9. onInit() {
10. console.info('PageA onInit');
11. },
12. onReady() {
13. console.info('PageA onReady');
14. },
15. onShow() {
16. console.info('PageA onShow');
17. },
18. onHide() {
19. console.info('PageA onHide');
20. },
21. onDestroy() {
22. console.info('PageA onDestroy');
23. },
24. onBackPress() {
25. console.info('PageA onBackPress');
26. },
27. onActive() {
28. console.info('PageA onActive');
29. },
30. onInactive() {
31. console.info('PageA onInactive');
32. },
33. onNewRequest() {
34. console.info('PageA onNewRequest');
35. }
36. }
```

pageB实现代码如下：

```
1. <!-- pageB.hml -->
2. <div class="container">
3. <text class="title">This is PageB</text>
4. </div>
```

```
1. /* pageB.css */
2. .container {
3. flex-direction: column;
4. align-items: center;
5. width: 100%;
6. height: 100%;
7. }
8. .title {
9. font-size: 38px;
10. text-align: center;
11. width: 100%;
12. height: 40%;
13. }
```

```
1. // pageB.js
2. export default {
3. onInit() {
4. console.info('PageB onInit');
5. },
6. onReady() {
7. console.info('PageB onReady');
8. },
9. onShow() {
10. console.info('PageB onShow');
11. },
12. onHide() {
13. console.info('PageB onHide');
14. },
15. onDestroy() {
16. console.info('PageB onDestroy');
17. },
18. onBackPress() {
19. console.info('PageB onBackPress');
20. },
21. onActive() {
22. console.info('PageB onActive');
23. },
24. onInactive() {
25. console.info('PageB onInactive');
26. },
27. onNewRequest() {
28. console.info('PageB onNewRequest');
29. }
30. }
```

运行程序，通过日志观察生命周期函数的调用顺序。其中pageA的生命周期函数的调用顺序为：

* 打开应用进入页面A：onInit() -> onReady() -> onActive() -> onShow()
* 在页面A打开页面B：onHide()
* 从页面B返回页面A：onShow()
* 退出页面A：onBackPress() -> onInactive() -> onHide()
* 页面A隐藏到后台运行：onInactive() -> onHide()
* 页面A从后台运行恢复到前台：onNewRequest() -> onShow() -> onActive()

pageB的生命周期函数的调用顺序为：

* 在页面A打开页面B：onInit() -> onReady() -> onShow()
* 从页面B返回页面A：onBackPress() -> onHide() -> onDestroy()
* 页面B隐藏到后台运行：onInactive() -> onHide()
* 页面B从后台运行恢复到前台：onNewRequest() -> onShow() -> onActive()
