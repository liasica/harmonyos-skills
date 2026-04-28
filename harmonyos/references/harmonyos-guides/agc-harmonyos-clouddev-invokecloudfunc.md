---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudfunc
title: 在端侧调用云函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发端侧工程 > 在端侧调用云侧代码 > 在端侧调用云函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:08+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a86f7a7863fea7329bece547869238c38b9d6c808f1df1c4a149cd7e62c12ca8
---

## 前提条件

请确保[云函数已正确开发并部署](agc-harmonyos-clouddev-deployfunc.md)。

## 操作步骤

1. 在代码文件中引入Cloud Foundation Kit。

   ```
   1. import { cloudFunction } from '@kit.CloudFoundationKit'
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用您云侧部署的云函数。关于云函数接口的更详细信息，请参考[Cloud Foundation Kit API参考-云函数模块](../harmonyos-references/cloudfoundation-cloudfunction.md)。

   ```
   1. //填入需要调用的云函数名称
   2. cloudFunction.call({name: 'xxxx'})
   3. .then((res: cloudFunction.FunctionResult) => {
   4. // 处理调用返回
   5. }).catch((err: BusinessError) => {
   6. // 调用云函数异常时的处理逻辑
   7. })
   ```

   例如，调用云侧函数“my-cloud-function”，以返回一个时间戳。

   ```
   1. import { cloudFunction } from '@kit.CloudFoundationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. interface result {
   5. intervalTime: number
   6. }

   8. interface res {
   9. result: result
   10. }

   12. @Entry
   13. @Component
   14. struct CloudFunction {
   15. @State globalId: string = '';

   17. build() {
   18. Column() {
   19. Navigation()
   20. .title($r('app.string.cloud_function_title'))
   21. .height('50vp')
   22. .width('100%')
   23. .margin({ bottom: 10 })
   24. .titleMode(NavigationTitleMode.Mini)

   26. Text($r('app.string.cloud_function_description'))
   27. .width('90%')
   28. .textAlign(TextAlign.Center)
   29. .margin({ top: 20, bottom: 20 })
   30. .fontSize($r('app.float.body_font_size'))
   31. Button({ type: ButtonType.Normal }) {
   32. Text($r('app.string.cloud_function_button_text'))
   33. .fontColor($r('app.color.white'))
   34. .margin({ top: 5, bottom: 5 })
   35. }
   36. .width('90%')
   37. .borderRadius('8vp')
   38. .height('30vp')
   39. .margin({ top: 10 })
   40. .onClick(() => {
   41. this.callMyFunction()
   42. })

   44. Column() {
   45. Text(this.globalId).fontSize($r('app.float.body_font_size'))
   46. }
   47. .width('90%')
   48. .padding({ top: 20, bottom: 20 })
   49. .margin({ top: 20 })
   50. .backgroundColor($r('app.color.placeholder_background'))
   51. }.height('100%')
   52. }

   54. callMyFunction() {
   55. cloudFunction.call({ name: 'my-cloud-function' }).then((res: cloudFunction.FunctionResult) => {
   56. let callback  = res as res;
   57. console.info(`Succeeded in call the function, time:${callback.result.intervalTime} `);
   58. }).catch((err: BusinessError) => {
   59. console.error(`Failed to call the function, Code: ${err.code}, message: ${err.message}`);
   60. });
   61. }
   62. }
   ```
