---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-b112
title: OS平台API行为的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > OS平台行为变更说明 > HarmonyOS 5.0.1(13) Release引入的行为变更 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-04-29T13:23:53+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:53483d6207b9ba667adcbf5b7e744e5eae76741e3ca13b764c6f990a2767eac0
---

## ArkUI

### 鼠标按键处理行为变更

**变更原因**

在开发者为组件配置鼠标事件后，若在组件区域内按下鼠标非左键并拖拽至组件区域外释放，此时将无法接收到按键释放事件，这可能导致事件配对失败，进而引发应用程序行为异常。此变更确保开发者能够接收到匹配的按键按下与释放事件。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.1(13)时生效。

变更前：在开发者为组件配置了鼠标事件后，如果在组件区域内按下鼠标非左键，并将鼠标移动至组件区域外再释放按键，此时将无法接收到按键释放事件。

变更后：在开发者为组件配置了鼠标事件后，如果在组件区域内按下鼠标非左键，并将鼠标移动至组件区域外再释放按键，此时可以接收到按键释放事件。

**起始API Level**

8

**变更的接口/组件**

ArkTS的onMouse接口，Native的OH\_NativeXComponent\_GetMouseEvent接口和registerNodeEvent接口的NODE\_ON\_MOUSE。

**适配指导**

默认行为变更，应注意变更后的行为是否对整体应用逻辑产生影响。

### 动画接口在播放次数为无限循环时的行为变更

**变更原因**

非动画的闭包函数修改状态变量，存在被带入无限循环动画的风险，产生预期外的无限循环动画且无法停止。

**变更影响**

此变更涉及应用适配。

变更前：在调用无限循环动画接口（例如：无限循环的animateTo）时，首次布局过程中触发的同步回调里所做的修改，会被纳入无限循环动画中，从而产生多余的动画。

变更后：在调用无限循环动画接口（例如：无限循环的animateTo）时，首次布局过程中触发的同步回调里所做的修改，系统至多做2次额外刷新保护，避免动画前的同步回调被纳入无限循环动画中，对于2次额外刷新仍不能保护住的同步回调，和原行为一致也会产生无限循环动画。

**起始API Level**

* animateTo：7
* animateToImmediately：12
* UIContext.keyframeAnimateTo：11
* UIContext.animateTo：11
* UIContext.animateToImmediately：12

**变更的接口/组件**

1、animateTo；

2、animateToImmediately；

3、UIContext.keyframeAnimateTo；

4、UIContext.animateTo；

5、UIContext.animateToImmediately；

**适配指导**

为了创建无限循环的动画，必须明确地将修改操作置于动画接口（例如：无限循环的animateTo）的闭包函数内。

animateTo适配前：

```
1. @Entry
2. @Component
3. struct Example {
4. @State rotateAngle: number = 0
5. @State wid: number = 100
6. @State color: Color = Color.Red

8. build() {
9. Column() {
10. Column()
11. .size({width: 100, height: 100})
12. .backgroundColor(this.color)
13. Button('animate')
14. .margin(50)
15. .rotate({ x: 0, y: 0, z: 1, angle: this.rotateAngle })
16. .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions)=>{
17. // animateTo前修改wid时的布局同步的触发了onSizeChange事件，也会被带入无限循环动画中
18. // 产生背景色的无限循环动画
19. if (Number(newValue.width) >= 150) {
20. this.color = Color.Blue;
21. } else {
22. this.color = Color.Red;
23. }
24. })
25. .onClick(()=>{
26. this.wid = 200;
27. animateTo({
28. iterations: -1, // 设置-1表示动画无限循环
29. playMode: PlayMode.Alternate,
30. }, () => {
31. this.rotateAngle = 90
32. })
33. })
34. }.width('100%').margin({ top: 5 })
35. }
36. }
```

animateTo适配后：

```
1. @Entry
2. @Component
3. struct Example {
4. @State rotateAngle: number = 0
5. @State wid: number = 100
6. @State color: Color = Color.Red

8. build() {
9. Column() {
10. Column()
11. .size({width: 100, height: 100})
12. .backgroundColor(this.color)
13. Button('animate')
14. .margin(50)
15. .rotate({ x: 0, y: 0, z: 1, angle: this.rotateAngle })
16. .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions)=>{
17. // onSizeChange为同步回调，最好不在同步回调中直接修改状态变量。
18. })
19. .onClick(()=>{
20. this.wid = 200;
21. // 如果不需要产生color的动画则在动画外直接修改color，this.color = Color.Blue，而不是在同步回调中
22. animateTo({
23. iterations: -1, // 设置-1表示动画无限循环
24. playMode: PlayMode.Alternate,
25. }, () => {
26. this.rotateAngle = 90
27. // 如果需要产生color的动画则在此处加上this.color = Color.Blue，将color的改变放在动画闭包中
28. })
29. })
30. }.width('100%').margin({ top: 5 })
31. }
32. }
```

### 系统对单应用最大创建UIAbility数量限制变更

**变更原因**

系统防护机制增强，系统会针对设备上单应用最大创建UIAbility数量进行限制，如果数量超过限制，系统可能会将最早未使用的任务删除。

**变更影响**

此变更需要适配。

变更前：单应用最大创建UIAbility数量限制为128。

变更后：手机及平板单应用最大创建UIAbility数量限制默认为10，具体限制数由产品配置。

当单个应用创建UIAbility数量超过限制时，再次启动新的任务系统可能会将最早未使用的任务删除。

**起始API Level**

不涉及

**变更的接口/组件**

任务管理规格

**适配指导**

系统针对单应用有最大UIAbility数量限制机制，应用开发需保证正常使用情况下任务数量不超过系统限制；如果超过，再次启动新的UIAbility任务时系统会将最早未使用的任务删除，该情况下需保证删除最早的任务不影响应用正常功能。

### Video组件不再默认解析并自动播放拖拽信息中的视频资源

**变更原因**

Video组件默认允许拖入任意视频并自动播放的行为不符合终端用户预期，故需调整该默认规格。

说明

该变更在2025年1月8日更新的ROM版本引入，ROM版本号为5.0.0.123。

**变更影响**

变更前：Video组件默认解析并自动播放拖拽信息中的视频资源。

变更后：Video组件不会默认解析并自动播放拖拽信息中的视频资源。

**起始API Level**

10

**变更的接口/组件**

Video组件。

**适配指导**

应用若需要使Video组件支持解析拖入的视频信息并自动播放，可通过如下代码实现：

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

3. @Entry
4. @Component
5. struct Index {
6. @State videoSrc: Resource | string = $rawfile('video1.mp4');
7. private controller: VideoController = new VideoController();

9. build() {
10. Column() {
11. Video({
12. src: this.videoSrc,
13. controller: this.controller
14. })
15. .width('100%')
16. .height(600)
17. .onPrepared(() => {
18. // 在onPrepared回调中执行controller的start方法，确保视频源更换后直接开始播放。
19. this.controller.start();
20. })
21. .onDrop((e: DragEvent) => {
22. // 外部视频拖入应用Video组件范围，松手后触发通过onDrop注册的回调。
23. // 在DragEvent中会包含拖入的视频源信息，取出后赋值给状态变量videoSrc即可改变Video的视频源。
24. let record = e.getData().getRecords()[0];
25. if (record.getType() == uniformTypeDescriptor.UniformDataType.VIDEO) {
26. let videoInfo = record as unifiedDataChannel.Video;
27. this.videoSrc = videoInfo.videoUri;
28. }
29. })
30. }
31. }
32. }
```

## ArkWeb

### onErrorReceive接口在首次加载woff等在线字体资源不再触发的行为变更

**变更原因**

woff等在线字体资源首次加载时不再指定仅从缓存中读取。

**变更影响**

该变更为兼容性变更。

变更前：首次加载woff等在线字体资源时，会触发错误码为-400（ERR\_CACHE\_MISS）的onErrorReceive回调。

变更后：首次加载woff等在线字体资源时，不再触发错误码为-400（ERR\_CACHE\_MISS）的onErrorReceive回调。

**起始API Level**

8

**变更的接口/组件**

web.d.ts的onErrorReceive接口

**适配指导**

默认行为变更，应注意变更后的行为是否对整体应用逻辑产生影响。

## Form Kit

### PostCardAction的router事件允许拉起Ability类型范围变更

**变更原因**

PostCardAction的router事件当前未对被拉起的Ability类型进行校验，但实际此事件应只允许拉起UIAbility，针对使用router事件拉起非UIAbility的场景，需要做安全加固。

说明

该变更在2025年1月8日更新的ROM版本引入，ROM版本号为5.0.0.123。

**变更影响**

该变更为不兼容变更。

变更前：通过PostCardAction接口的router事件，可以拉起所有类型的Ability。

变更后：通过PostCardAction接口的router事件，仅允许拉起UIAbility。

**起始API Level**

9

**变更的接口/组件**

PostCardAction

**适配指导**

应用侧使用PostCardAction接口的router事件拉起Ability时，需确保拉起的目标Ability属于UIAbility。若需要拉起其他类型的Ability，建议通过其他类型的事件，例如message事件， 跳转到FormExtensionAbility内处理。

## 公共能力

### app.json中bundleName字段正则匹配规则修改

**变更原因**

app.json中对bundleName的正则匹配规则较简单，不符合应用包名规范，进行整改。

说明

该变更在2024年12月8日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.5.306。

**变更影响**

变更前，规则如下：

* 由字母、数字、下划线（\_）和符号“.”组成，且必须以字母开头。

变更后，规则如下：

* 由字母、数字、下划线和符号“.”组成。
* 必须为以点号（.）分隔的字符串，且至少包含三段。
* 首段以英文字母开头，非首段以数字或英文字母开头，每一段以数字或者英文字母结尾。
* 不允许多个点号（.）连续出现。

**起始API Level**

8

**变更的接口/组件**

Openharmony SDK目录下toolchains/modulecheck/app.json scheme文件。

**适配指导**

升级SDK版本后，如果DevEco Studio编辑器中提示如下报错，请按照新规则修改应用的bundleName。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/QGgNIY2gTAG4putVXu5_DQ/zh-cn_image_0000002143569014.png?HW-CC-KV=V1&HW-CC-Date=20260429T052352Z&HW-CC-Expire=86400&HW-CC-Sign=04047DDD44FE87661D74954D14178FF376E59745B8C169D60F64D9F00BC350EA)

## 工具

### 应用发生OOM时Heapdump产物文件格式变更

**变更原因**

为了提升应用发生OOM时Heapdump生成dump文件的概率和效率，支撑开发者定位内存泄漏问题：

1. 移除Heapdump在线解析逻辑，产物格式由.heapsnapshot变为.rawheap。
2. rawheap文件解析生成heapsnapshot文件的功能由SDK中集成的rawheap\_translator工具提供。

说明

该变更在2024年12月8日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.5.306。

**变更影响**

该变更为不兼容变更。

变更前：应用OOM时Heapdump生成dump文件的格式为.heapsnapshot。

变更后：应用OOM时Heapdump生成dump文件的格式为.rawheap，需要通过调用rawheap\_translator工具将rawheap文件解析转换为heapsnapshot文件。

**起始API Level**

11

**变更的接口/组件**

OpenHarmony的SDK在toolchains目录下新增rawheap\_translator工具。

**适配指导**

将当前应用OOM时Heapdump生成的rawheap文件转换成之前的heapsnapshot文件，需要使用设备或SDK中的rawheap\_translator工具

工具获取：

当前rawheap\_translator工具适配了OHOS、Windows、Linux、MacOS平台：

OHOS平台工具所在路径：/bin/rawheap\_translator, 可直接在设备中调用。

Windows、Linux、MacOS平台工具在SDK中获取，所在路径：/toolchains/rawheap\_translator。

环境变量设置：

Windows环境变量设置：

在此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量 > Path > 编辑中，将rawheap\_translator.exe的所在路径添加到Path中，配置完成后重启电脑。

MacOS环境变量设置：

打开终端工具，输入以下命令并执行：

```
1. echo $SHELL
```

上述命令执行结果可能为/bin/bash或者/bin/zsh，下面以/bin/bash为例，/bin/zsh同理。执行以下命令，打开.bash\_profile文件：

```
1. vi ~/.bash_profile
```

单击键盘上字母“i”，进入编辑模式，输入以下命令：

```
1. export PATH=$PATH:<rawheap_translator路径>
```

编辑完成后，单击键盘Esc键退出编辑模式，然后输入“:wq”，单击键盘Enter键保存修改。

执行以下命令，使配置的环境变量生效：

```
1. source ~/.bash_profile
```

配置完成后重新启动电脑。

使用方法：

工具调用命令：

```
1. rawheap_translator <rawheap_file>

3. rawheap_translator <rawheap_file> <heapsnapshot_file>
```

参数列表：

| 选项 | 描述 | 举例 |
| --- | --- | --- |
| <rawheap\_file> | 应用OOM时Heapdump生成的rawheap文件路径，例如：/data/log/reliability/resource\_leak/memory\_leak | 解析目录D:\temp\rawheap下的example.rawheap文件：rawheap\_translator D:\temp\example.rawheap |
| <heapsnapshot\_file> | 指定解析生成文件的路径和名称，文件后缀必须为heapsnapshot；若不指定则默认为当前路径，文件名自动生成 | 解析目录D:\temp\rawheap下的example.rawheap文件，并在D:\temp\result下生成结果文件result.heapsnapshot：rawheap\_translator D:\temp\example.rawheap D:\temp\result\result.heapsnapshot |
