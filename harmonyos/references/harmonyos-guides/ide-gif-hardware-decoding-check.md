---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-gif-hardware-decoding-check
title: @performance/gif-hardware-decoding-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/gif-hardware-decoding-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:02+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:cc9ac907d54c182cd438ca962cd0883d1a333521ff4d3fbbc25b843f59939786
---

在使用@ohos/gif-drawable库解码gif图片时，建议开启硬解码，提升gif加载性能。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/gif-hardware-decoding-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // @ohos/gif-drawable依赖可以通过'ohpm install @ohos/gif-drawable@2.1.0'下载安装
2. import { GIFComponentV2, ResourceLoader } from '@ohos/gif-drawable'

4. @Entry
5. @ComponentV2
6. struct GifDrawableNoReport0 {
7. @Local model2:GIFComponentV2.ControllerOptions = new GIFComponentV2.ControllerOptions();
8. @Local gifAutoPlay:boolean = false;
9. @Local gifReset:boolean = false;

11. aboutToAppear(): void {
12. this.model2.destroy();
13. let model22:GIFComponentV2.ControllerOptions = new GIFComponentV2.ControllerOptions();
14. // 调用setOpenHardware接口且值为true，开启硬解码
15. model22.setOpenHardware(true);
16. model22.setSpeedFactor(1);
17. ResourceLoader.downloadDataWithContext(this.getUIContext().getHostContext(), {
18. url: 'https://example.com/test.gif'
19. }, (sucBuffer: ArrayBuffer) => {
20. model22.loadBuffer(sucBuffer, () => {
21. console.log('网络加载解析成功回调绘制！')
22. this.gifAutoPlay = true;
23. // 给组件数据赋新的用户配置参数，达到后续gif动画效果
24. this.model2 = model22;
25. })
26. }, (err: string) => {
27. // 用户根据返回的错误信息，进行业务处理(展示一张失败占位图、再次加载一次、加载其它图片等)
28. })
29. }
30. build() {
31. Row() {
32. GIFComponentV2({model:this.model2!!, autoPlay:this.gifAutoPlay!!, resetGif: this.gifReset!!})
33. }
34. }
35. }
```

## 反例

```
1. // @ohos/gif-drawable依赖可以通过'ohpm install @ohos/gif-drawable@2.1.0'下载安装
2. import { GIFComponentV2, ResourceLoader } from '@ohos/gif-drawable'

4. @Entry
5. @ComponentV2
6. struct GifDrawableReport0 {
7. // 调用setOpenHardware接口且值为true，开启硬解码
8. // model0未调用setOpenHardware接口，告警
9. @Local model0: GIFComponentV2.ControllerOptions = new GIFComponentV2.ControllerOptions();
10. @Local gifAutoPlay:boolean = false;
11. @Local gifReset:boolean = false;

13. aboutToAppear(): void {
14. this.model0.destroy();
15. // model00未调用setOpenHardware接口，告警
16. let model00: GIFComponentV2.ControllerOptions = new GIFComponentV2.ControllerOptions();
17. model00.setSpeedFactor(1);
18. ResourceLoader.downloadDataWithContext(this.getUIContext().getHostContext(), {
19. url: 'https://example.com/test.gif'
20. }, (sucBuffer: ArrayBuffer) => {
21. model00.loadBuffer(sucBuffer, () => {
22. console.log('网络加载解析成功回调绘制！')
23. this.gifAutoPlay = true;
24. // 给组件数据赋新的用户配置参数，达到后续gif动画效果
25. this.model0 = model00;
26. })
27. }, (err: string) => {
28. // 用户根据返回的错误信息，进行业务处理(展示一张失败占位图、再次加载一次、加载其它图片等)
29. })
30. }
31. build() {
32. Row() {
33. GIFComponentV2({model:this.model0!!, autoPlay:this.gifAutoPlay!!, resetGif: this.gifReset!!})
34. }
35. }
36. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
