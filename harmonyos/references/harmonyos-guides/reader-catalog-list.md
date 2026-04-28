---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-catalog-list
title: 获取目录列表
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容解析 > 获取目录列表
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:895fdf69aad3c90a433a4a311cc1dc1da3aae2d5817e31b50a0f5ce9b2c1ebd1
---

当应用需要展示书籍目录列表时，开发者可通过解析能力获取目录节点列表，实现目录列表中章节名称按顺序、层级的展示。当用户点击目录节点时，开发者也需要获取目录位置及资源信息，用于跳转到指定位置。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/WrhgEQLcQ_-FyPaGpV15XA/zh-cn_image_0000002583479143.png?HW-CC-KV=V1&HW-CC-Date=20260427T235037Z&HW-CC-Expire=86400&HW-CC-Sign=4C5F2C50784591BAB95F6B6D88D34EC4C7055AFAC0703D86800A2BDFC0082427)

## 接口说明

获取目录列表及获取指定目录位置及资源信息共涉及4个接口，具体API说明请参考下表。

| 接口名 | 描述 |
| --- | --- |
| [getDefaultHandler](../harmonyos-references/reader-book-parser.md#getdefaulthandler)(path: string): Promise<BookParserHandler> | 获取书籍默认解析器。 |
| [getCatalogList](../harmonyos-references/reader-book-parser.md#getcataloglist)(): CatalogItem[] | 获取书籍目录列表。 |
| [getDomPosByCatalogHref](../harmonyos-references/reader-book-parser.md#getdomposbycataloghref)(href: string): string | 获取阅读起始位置domPos。 |
| [getSpineList](../harmonyos-references/reader-book-parser.md#getspinelist)(): SpineItem[] | 获取书脊内容列表。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { bookParser } from '@kit.ReaderKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 通过提前导入到[应用沙箱目录](app-sandbox-directory.md)中的书籍文件，初始化书籍解析器。

   ```
   1. private defaultHandler: bookParser.BookParserHandler | null = null;

   3. aboutToAppear(): void {
   4. this.init().then(() => {
   5. });
   6. }

   8. private async init() {
   9. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   10. let path: string = `${context.filesDir}/abc.epub`;
   11. try {
   12. this.defaultHandler = await bookParser.getDefaultHandler(path);
   13. } catch (error) {
   14. hilog.error(0x0000, "testTAG", `getDefaultHandler failed, Code: ${error.code}, message: ${error.message}`);
   15. }
   16. }
   ```
3. 获取目录列表并进行展示。

   ```
   1. @State catalogItemList: bookParser.CatalogItem[] = [];

   3. aboutToAppear(): void {
   4. this.init().then(() => {
   5. this.getCatalogList();
   6. });
   7. }

   9. private getCatalogList() {
   10. try {
   11. this.catalogItemList = this.defaultHandler?.getCatalogList() || [];
   12. } catch (error) {
   13. hilog.error(0x0000, "testTAG", `getCatalogList failed, Code: ${error.code}, message: ${error.message}`);
   14. }
   15. }

   17. build() {
   18. Column() {
   19. List() {
   20. ForEach(this.catalogItemList, (item: bookParser.CatalogItem) => {
   21. ListItem() {
   22. Column() {
   23. Row() {
   24. Row() {
   25. Text(' · ')
   26. .fontSize(14)
   27. Text(item.catalogName)
   28. .fontSize(14)
   29. .textOverflow({ overflow: TextOverflow.Ellipsis })
   30. .padding({ top: 8, bottom: 8 })
   31. .maxLines(2)
   32. .layoutWeight(1)
   33. }

   35. }
   36. .width('100%')
   37. .height(48)
   38. .justifyContent(FlexAlign.Center)
   39. .alignItems(VerticalAlign.Center)

   41. Divider()
   42. }
   43. .padding({
   44. left: item.catalogLevel ? item.catalogLevel * 26 : 10,
   45. right: item.catalogLevel ? item.catalogLevel * 26 : 10,
   46. top: 6,
   47. bottom: 6
   48. })
   49. .onClick(async () => {
   50. // 在此实现点击目录跳转到指定章节功能
   51. this.jumpToCatalogItem(item);
   52. })
   53. }
   54. })
   55. }
   56. .scrollBar(BarState.Off)
   57. .width('100%')
   58. .height('100%')
   59. }
   60. .width('100%')
   61. .height('100%')
   62. }
   ```
4. 获取跳转用的目录位置及资源信息。

   ```
   1. private jumpToCatalogItem(catalogItem: bookParser.CatalogItem) {
   2. let domPos = this.getDomPos(catalogItem);
   3. let resourceIndex = this.getResourceItemByCatalog(catalogItem).index;
   4. // 通过domPos及resourceIndex信息，即可通过startPlay接口跳转到指定位置
   5. hilog.info(0x0000, "testTAG", `jumpToCatalogItem domPos:${domPos}, resourceIndex:${resourceIndex}`);
   6. }

   8. private getDomPos(catalogItem: bookParser.CatalogItem): string {
   9. try {
   10. let domPos: string = this.defaultHandler?.getDomPosByCatalogHref(catalogItem.href || '') || '';
   11. return domPos;
   12. } catch (error) {
   13. hilog.error(0x0000, "testTAG", `getDomPos failed, Code: ${error.code}, message: ${error.message}`);
   14. }
   15. return '';
   16. }

   18. /**
   19. * 获取书籍目录对应的资源条目
   20. *
   21. * @param catalogItem 目录条目
   22. */
   23. private getResourceItemByCatalog(catalogItem: bookParser.CatalogItem): bookParser.SpineItem {
   24. let resourceFile = catalogItem.resourceFile || '';
   25. try {
   26. let spineList: bookParser.SpineItem[] = this.defaultHandler?.getSpineList() || []
   27. // 查找目录对应的资源条目
   28. let resourceItemArr = spineList.filter(item => item.href === resourceFile);
   29. if (resourceItemArr.length > 0) {
   30. hilog.info(0x0000, 'testTag', 'getResourceItemByCatalog get resource ', resourceItemArr[0]);
   31. let resourceItem = resourceItemArr[0];
   32. return resourceItem;
   33. } else if (spineList.length > 0) {
   34. // 如果查找不到，则默认返回第1个资源条目
   35. hilog.info(0x0000, 'testTag', 'getResourceItemByCatalog get resource in resourceList', spineList[0]);
   36. return spineList[0];
   37. }
   38. } catch (error) {
   39. hilog.error(0x0000, "testTAG", `getDomPos failed, Code: ${error.code}, message: ${error.message}`);
   40. }
   41. // 如果没有资源条目，则返回默认值
   42. hilog.info(0x0000, 'testTag', 'getResourceItemByCatalog get resource in escape');
   43. return {
   44. idRef: '',
   45. index: 0,
   46. href: '',
   47. properties: ''
   48. };
   49. }
   ```
