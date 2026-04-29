---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-email-apps-by-mailto
title: 拉起邮件类应用（mailto方式）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定类型的应用 > 拉起邮件类应用（mailto方式）
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b1623f52c988718d3bc27ff71bdbd7e65f5a4e0d361b8e6ba7f1d59a9053084
---

## 使用场景

通过mailto电子邮件协议，可以创建指向电子邮件地址的超链接，方便用户通过网页或应用中的超链接直接跳转电子邮件应用。同时，支持在mailto:的相关字段中定义邮件的收件人、主题、正文内容等，节省用户编辑邮件的时间。

常见的应用场景举例如下：

* 从网页拉起：
  + 用户在购物网站浏览产品页面时，看到“联系我们”按钮，点击后会拉起默认邮件客户端。收件人自动填写为客服邮箱，邮件主题设定为产品咨询。
  + 在招聘岗位页面，点击“申请职位”按钮，会拉起邮件客户端。收件人地址为招聘邮箱，邮件主题为“应聘某职位”，正文可以预先填入申请模板。
* 从应用拉起：
  + 移动应用中，用户点击“反馈”按钮时，应用调用系统功能，拉起默认邮件客户端，预先填写反馈邮箱、问题描述等信息。
  + 移动应用中，当用户点击“通过邮件分享”按钮时，应用会通过 mailto 调用邮件客户端，预填邮件主题和正文。

    说明

    - 如果使用mailto方式拉起邮件应用，需要拉起方先按mailto格式封装字符串，再使用mailto方式拉起。邮件应用会解析收到的mailto协议字符串，并填充发件人、收件人、邮件内容等信息。
    - 如果拉起方已知发件人、收件人、邮件内容等信息，推荐[使用startAbilityByType方式拉起邮件应用](start-email-apps.md)。

## mailto协议格式

mailto协议标准格式如下：

```
1. mailto:someone@example.com?key1=value1&key2=value2
```

* mailto:：mailto scheme，必填。
* someone@example.com：收件人地址，选填。如果存在多个地址，用英文逗号分隔。
* ?：邮件头声明开始符号。如果带邮件头参数，则必填。
* key-value：邮件头参数，详细参数见下表。

  | 邮件头 | 含义 | 数据类型 | 是否必填 |
  | --- | --- | --- | --- |
  | subject | 邮件主题 | string | 否 |
  | body | 邮件正文 | string | 否 |
  | cc | 抄送人，多个用逗号分隔 | string | 否 |
  | bcc | 密送人，多个用逗号分隔 | string | 否 |

特殊符号处理：

如果邮件头参数值中存在特殊字符，如@、?、=、&等符号，可能导致配置不生效。建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。

常用符号替换为ASCII码的对照表如下：

| 特殊符号 | : | @ | ? | = | & | # | $ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 替换编码 | %3A | %40 | %3F | %3D | %26 | %23 | %24 |

## 拉起方开发步骤

### 从网页拉起

网页中的超链接需要满足mailto协议。示例如下：

```
1. <a href="mailto:support@example.com?subject=Product Inquiry&body=I am interested in...">联系我们</a>
```

实际开发时，需要将邮箱地址替换为真实的邮箱，邮件内容可以根据需要进行配置。

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/h3D6rDN4SxWQxR3vgH3uXQ/zh-cn_image_0000002589243803.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052552Z&HW-CC-Expire=86400&HW-CC-Sign=E2906189BC5704E1CA13F5592DC1A43C4B8FC8AD4BFDF67923AA63371876ED9C)

### 从应用拉起

保证mailto字符串传入uri参数即可，在应用中page页面可通过 getHostContext() 获取context，在ability中可通过this.context获取context。

```
1. import { common } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column() {
8. Button('反馈')
9. .onClick(() => {
10. let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
11. ctx.startAbility({
12. action: 'ohos.want.action.sendToData',
13. uri: 'mailto:feedback@example.com?subject=App Feedback&body=Please describe your feedback here...'
14. })
15. })
16. }
17. }
18. }
```

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/-wLnrddOTc6sv0twPnGaLQ/zh-cn_image_0000002558763998.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052552Z&HW-CC-Expire=86400&HW-CC-Sign=F5F77A95FB24ABD4E00967C73B82D77225B8A3DEDE62304915FDAB4A2F4D916A)

## 目标方开发步骤

1. 为了能够支持被其他应用通过mailto协议拉起，目标应用需要在[module.json5配置文件](module-configuration-file.md)中声明mailto。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. // ...
   7. "skills": [
   8. {
   9. "actions": [
   10. 'ohos.want.action.sendToData'
   11. ],
   12. "uris": [
   13. {
   14. "scheme": "mailto",
   15. // linkFeature 用于适配垂类面板拉起
   16. "linkFeature": 'ComposeMail'
   17. }
   18. ]
   19. }
   20. ]
   21. }
   22. ]
   23. }
   24. }
   ```
2. 目标应用在代码中取出uri参数进行解析。

   ```
   1. export default class EntryAbility extends UIAbility {
   2. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   3. // 应用冷启动生命周期回调，其他业务处理...
   4. this.parseMailto(want);
   5. }

   7. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   8. // 应用热启动生命周期回调，其他业务处理...
   9. this.parseMailto(want);
   10. }

   12. public parseMailto(want: Want) {
   13. const uri = want?.uri;
   14. if (!uri || uri.length <= 0) {
   15. return;
   16. }
   17. // 开始解析 mailto...
   18. }
   19. }
   ```
