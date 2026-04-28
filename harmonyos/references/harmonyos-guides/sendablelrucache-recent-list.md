---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendablelrucache-recent-list
title: 获取最近访问列表场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 获取最近访问列表场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c9014eace37ec0ee0ba402420db3187dd41ca7e5802004ef3fe5474dc282e6e1
---

为了快速访问最近使用的[Sendable](arkts-sendable.md)对象，从API version 18开始，ArkTS引入了[SendableLruCache](../harmonyos-references/arkts-apis-arkts-utils-sendablelrucache.md)。开发者可以通过向SendableLruCache实例中添加、删除和获取Sendable对象，实现快速访问最近使用的Sendable对象。本文提供使用SendableLruCache实现获取最近使用列表的开发指导，以书架为例，每次打开一本图书后，需将图书信息更新到最近访问列表中，并在下次访问书架页面时显示最近访问的图书列表。

说明

使用SendableLruCache实例对象时需加锁，避免多线程同时操作导致数据不一致。

存放到SendableLruCache实例中的对象必须是Sendable对象。

1. 创建SendableLruCache实例对象，并根据业务需求预设最大容量。

   此例设置SendableLruCache实例的最大容量为4，用SendableClass类管理，并导出SendableClass类实例对象。

   ```
   1. // LruCache.ets
   2. import { ArkTSUtils } from '@kit.ArkTS';

   4. // 使用use shared标记为共享模块
   5. 'use shared'

   7. // SendableClass实例对象在不同线程间可共享
   8. @Sendable
   9. class SendableClass {
   10. // 使用SendableLruCache实例对象时需加锁，避免多线程同时操作导致数据不一致
   11. private lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();
   12. private books_: ArkTSUtils.SendableLruCache<string, string> = new ArkTSUtils.SendableLruCache<string, string>(4);

   14. constructor() {
   15. this.books_.put('fourth', 'Book4');
   16. this.books_.put('third', 'Book3');
   17. this.books_.put('second', 'Book2');
   18. this.books_.put('first', 'Book1');
   19. }

   21. // 封装put、get、keys方法，加锁操作
   22. public async put(key: string, value: string) {
   23. await this.lock_.lockAsync(() => {
   24. this.books_.put(key, value);
   25. })
   26. }

   28. public async get(key: string): Promise<string | undefined> {
   29. return this.lock_.lockAsync(() => {
   30. return this.books_.get(key);
   31. });
   32. }

   34. public async keys(): Promise<string[]> {
   35. return this.lock_.lockAsync(() => {
   36. return this.books_.keys();
   37. });
   38. }
   39. }

   41. export let lruCache = new SendableClass();
   ```
2. 在Index.ets页面同目录下创建4个图书页面，每个页面显示相应的图书信息，并将每个页面的路径注册到src/main/resources/base/profile/main\_pages.json文件中。

   ```
   1. // Book1.ets
   2. @Entry
   3. @Component
   4. struct Index1 {
   5. @State message: string = 'Hello World!';

   7. build() {
   8. RelativeContainer() {
   9. Text('第一本书的内容')
   10. .id('first book')
   11. .fontSize(20)
   12. .padding(10)
   13. .fontWeight(FontWeight.Bold)
   14. .alignRules({
   15. center: { anchor: 'container', align: VerticalAlign.Center },
   16. middle: { anchor: 'container', align: HorizontalAlign.Center }
   17. })
   18. Button('返回')
   19. .fontSize(20)
   20. .padding(10)
   21. .fontWeight(FontWeight.Bold)
   22. .position({ x: '50%' })
   23. .onClick(() => {
   24. this.getUIContext().getRouter().pushUrl({ url: 'pages/GetRecentList' });
   25. })
   26. }
   27. .height('100%')
   28. .width('100%')
   29. }
   30. }
   ```

   ```
   1. // Book2.ets
   2. @Entry
   3. @Component
   4. struct Index2 {
   5. @State message: string = 'Hello World!';

   7. build() {
   8. RelativeContainer() {
   9. Text('第二本书的内容')
   10. .id('second book')
   11. .fontSize(20)
   12. .padding(10)
   13. .fontWeight(FontWeight.Bold)
   14. .alignRules({
   15. center: { anchor: 'container', align: VerticalAlign.Center },
   16. middle: { anchor: 'container', align: HorizontalAlign.Center }
   17. })
   18. Button('返回')
   19. .fontSize(20)
   20. .padding(10)
   21. .fontWeight(FontWeight.Bold)
   22. .position({ x: '50%' })
   23. .onClick(() => {
   24. this.getUIContext().getRouter().pushUrl({ url: 'pages/GetRecentList' });
   25. })
   26. }
   27. .height('100%')
   28. .width('100%')
   29. }
   30. }
   ```

   ```
   1. // Book3.ets
   2. @Entry
   3. @Component
   4. struct Index3 {
   5. @State message: string = 'Hello World!';

   7. build() {
   8. RelativeContainer() {
   9. Text('第三本书的内容')
   10. .id('third book')
   11. .fontSize(20)
   12. .padding(10)
   13. .fontWeight(FontWeight.Bold)
   14. .alignRules({
   15. center: { anchor: 'container', align: VerticalAlign.Center },
   16. middle: { anchor: 'container', align: HorizontalAlign.Center }
   17. })
   18. Button('返回')
   19. .fontSize(20)
   20. .padding(10)
   21. .fontWeight(FontWeight.Bold)
   22. .position({ x: '50%' })
   23. .onClick(() => {
   24. this.getUIContext().getRouter().pushUrl({ url: 'pages/GetRecentList' });
   25. })
   26. }
   27. .height('100%')
   28. .width('100%')
   29. }
   30. }
   ```

   ```
   1. // Book4.ets
   2. @Entry
   3. @Component
   4. struct Index4 {
   5. @State message: string = 'Hello World!';

   7. build() {
   8. RelativeContainer() {
   9. Text('第四本书的内容')
   10. .id('fourth book')
   11. .fontSize(20)
   12. .padding(10)
   13. .fontWeight(FontWeight.Bold)
   14. .alignRules({
   15. center: { anchor: 'container', align: VerticalAlign.Center },
   16. middle: { anchor: 'container', align: HorizontalAlign.Center }
   17. })
   18. Button('返回')
   19. .fontSize(20)
   20. .padding(10)
   21. .fontWeight(FontWeight.Bold)
   22. .position({ x: '50%' })
   23. .onClick(() => {
   24. this.getUIContext().getRouter().pushUrl({ url: 'pages/GetRecentList' });
   25. })
   26. }
   27. .height('100%')
   28. .width('100%')
   29. }
   30. }
   ```

   ```
   1. // main_pages.json

   3. {
   4. "src": [
   5. "pages/Index",
   6. "pages/Book1",
   7. "pages/Book2",
   8. "pages/Book3",
   9. "pages/Book4",
   10. "pages/GetRecentList"
   11. ]
   12. }
   ```
3. 访问书架页面时，自动展示最近访问的图书列表。

   ```
   1. // GetRecentList.ets
   2. import { taskpool } from '@kit.ArkTS';
   3. import { lruCache } from '../utils/LruCache'
   4. // ...

   6. @Concurrent
   7. async function updateBooks(key: string, value: string) {
   8. // 在子线程更新最近访问列表
   9. await lruCache.put(key, value);
   10. }

   12. @Entry
   13. @Component
   14. struct GetRecentList {
   15. @State message: string = '书架';
   16. @State books: string[] = [];

   18. async aboutToAppear () {
   19. // 自动获取最近访问的图书列表
   20. this.books = await lruCache.keys();
   21. }

   23. build() {
   24. Column({ space: 1 }) {
   25. Text(this.message)
   26. .id('HelloWorld')
   27. .fontSize(50)
   28. .fontWeight(FontWeight.Bold)
   29. .alignRules({
   30. center: { anchor: 'container', align: VerticalAlign.Center },
   31. middle: { anchor: 'container', align: HorizontalAlign.Center }
   32. })
   33. Button(this.books[3])
   34. .fontSize(20)
   35. .padding(10)
   36. .fontWeight(FontWeight.Bold)
   37. .onClick(async () => {
   38. // 获取绑定的图书信息
   39. let value = await lruCache.get(this.books[3]);
   40. // 更新最近访问列表
   41. taskpool.execute(updateBooks, this.books[3], value);
   42. this.getUIContext().getRouter().pushUrl({ url: 'pages/' + value });
   43. })
   44. Button(this.books[2])
   45. .fontSize(20)
   46. .padding(10)
   47. .fontWeight(FontWeight.Bold)
   48. .onClick(async () => {
   49. // 获取绑定的图书信息
   50. let value = await lruCache.get(this.books[2]);
   51. // 更新最近访问列表
   52. taskpool.execute(updateBooks, this.books[2], value);
   53. this.getUIContext().getRouter().pushUrl({ url: 'pages/' + value });
   54. })
   55. Button(this.books[1])
   56. .fontSize(20)
   57. .padding(10)
   58. .fontWeight(FontWeight.Bold)
   59. .onClick(async () => {
   60. // 获取绑定的图书信息
   61. let value = await lruCache.get(this.books[1]);
   62. // 更新最近访问列表
   63. taskpool.execute(updateBooks, this.books[1], value);
   64. this.getUIContext().getRouter().pushUrl({ url: 'pages/' + value });
   65. })
   66. Button(this.books[0])
   67. .fontSize(20)
   68. .padding(10)
   69. .fontWeight(FontWeight.Bold)
   70. .onClick(async () => {
   71. // 获取绑定的图书信息
   72. let value = await lruCache.get(this.books[0]);
   73. // 更新最近访问列表
   74. taskpool.execute(updateBooks, this.books[0], value);
   75. this.getUIContext().getRouter().pushUrl({ url: 'pages/' + value });
   76. })
   77. // ...
   78. }
   79. .height('100%')
   80. .width('100%')
   81. }
   82. }
   ```
