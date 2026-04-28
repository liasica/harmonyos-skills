---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-430
title: NavPathStack清空页面栈或者按返回键，为什么显示的是导航栏，如何实现退出Navigation所在的页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > NavPathStack清空页面栈或者按返回键，为什么显示的是导航栏，如何实现退出Navigation所在的页面
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fe6075d10024c5d2845592659a3299e8a3f5b5a8668165af032d1f02e7e062fa
---

**问题描述**

NavPathStack清空页面栈或者按返回键，为什么没有退出Navigation所在的页面，而是显示导航栏。

**解决措施**

因为Navigation隐藏导航栏的属性hideNavBar默认值为false，调用路由栈的pop时均会返回到导航栏NavBar，由于hideNavBar默认false，当调用pop()时系统会优先显示Navigation组件自带的导航栏，而非完全退出页面栈。

开发者可通过隐藏导航栏或重写返回键的方法，实现不返回导航栏。

* 设置Navigation属性[hideNavBar](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)为true，隐藏返回导航栏。
* 使用[onBackPressed()](../harmonyos-references/ts-basic-components-navdestination.md#onbackpressed10)方法重写返回键逻辑，通过[router.back()](../harmonyos-references/arkts-apis-uicontext-router.md#back)退出Navigation所在的页面。

  ```
  1. @Entry
  2. @Component
  3. struct NavPathStackExitsTheNavigationPage {
  4. @Provide('pathInfos') pathInfos: NavPathStack = new NavPathStack();

  6. @Builder
  7. myRouter(name: string) {
  8. if (name === 'PageOne') {
  9. PageOne()
  10. }
  11. }

  13. aboutToAppear(): void {
  14. this.pathInfos.pushPath({ name: 'PageOne' });
  15. }

  17. build() {
  18. Navigation(this.pathInfos) {
  19. Column() {
  20. Button('Jump to PageOne')
  21. .width('100%')
  22. .borderRadius(20)
  23. .margin({ bottom: 16 })
  24. .backgroundColor('#0A59F7')
  25. .onClick(() => {
  26. this.pathInfos.pushPath({ name: 'PageOne' });
  27. })
  28. }
  29. .width('100%')
  30. .height('100%')
  31. .padding({
  32. left: 16,
  33. right: 16
  34. })
  35. .justifyContent(FlexAlign.End)
  36. .alignItems(HorizontalAlign.Center)
  37. }
  38. .width('100%')
  39. .mode(NavigationMode.Auto)
  40. .title('title')
  41. .titleMode(NavigationTitleMode.Mini)
  42. .navDestination(this.myRouter)
  43. .hideBackButton(true)
  44. .hideNavBar(true) // Set the Navigation property's hideNavBar to true.
  45. }
  46. }

  48. @Component
  49. export struct PageOne {
  50. @Consume('pathInfos') pathInfos: NavPathStack;

  52. build() {
  53. NavDestination() {
  54. Column() {
  55. Text('PageOne')
  56. .width('100%')
  57. .fontSize(20)
  58. .fontColor(0x333333)
  59. .textAlign(TextAlign.Center)
  60. }
  61. .size({ width: '100%', height: '100%' })
  62. .alignItems(HorizontalAlign.Center)
  63. .justifyContent(FlexAlign.Center)
  64. }
  65. .title('PageOne')
  66. .onBackPressed(() => {
  67. this.getUIContext().getRouter().back(); // Override the return button logic to exit the navigation page.
  68. return true;
  69. })
  70. }
  71. }
  ```

  [NavPathStackExitsTheNavigationPage.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/NavPathStackExitsTheNavigationPage.ets#L21-L92)
