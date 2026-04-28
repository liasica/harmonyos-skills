---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-12
title: 怎么获取应用已使用的缓存大小，如何使用API清理缓存
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 怎么获取应用已使用的缓存大小，如何使用API清理缓存
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:23+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:5c57f285f2ece0c700e3d1a252a4d8619fd9fc6e72514e2bb08d45cb2bbdbbe8
---

**解决措施**

获取应用已使用缓存大小可以通过[storageStatistics.getCurrentBundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9)来获取。清理缓存需要调用context的cacheDir获取缓存，然后调用系统[@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md) 接口，判断是文件或者文件夹，再分别删除缓存。

如果需要删除整个应用的缓存，必须使用以下代码对所有模块级和应用级的Context进行操作。

**参考代码**

```
1. import { fileIo, storageStatistics } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct ClearCache {
7. // Create a file in the cache
8. writeFile() {
9. let filePath = this.getUIContext().getHostContext()!.cacheDir + '/test.txt';
10. let fileStream = fileIo.createStreamSync(filePath, 'w+');
11. fileStream.writeSync('1145141919810');
12. fileStream.close();
13. }

15. // Obtain the size of the application data space
16. getCache() {
17. storageStatistics.getCurrentBundleStats((error: BusinessError, bundleStats: storageStatistics.BundleStats) => {
18. if (error) {
19. console.error('getCurrentBundleStats failed with error:' + JSON.stringify(error));
20. } else {
21. console.info('getCurrentBundleStats successfully:' + JSON.stringify(bundleStats));
22. console.info('appsize :' + bundleStats.appSize);
23. console.info('cacheSize :' + bundleStats.cacheSize);
24. console.info('dataSize :' + bundleStats.dataSize);
25. }
26. });
27. }

29. // Clear cache
30. clearCache() {
31. let cacheDir = this.getUIContext().getHostContext()!.cacheDir;
32. console.info(cacheDir);

34. fileIo.listFile(cacheDir).then((filenames) => {
35. for (let i = 0; i < filenames.length; i++) {
36. let dirPath = cacheDir + '/' + filenames[i];
37. console.log(dirPath);
38. // Determine whether it is a folder
39. let isDirectory: boolean = false;
40. try {
41. isDirectory = fileIo.statSync(dirPath).isDirectory();
42. } catch (e) {
43. console.error(JSON.stringify(e));
44. }

46. if (isDirectory) {
47. fileIo.rmdirSync(dirPath);
48. } else {
49. fileIo.unlink(dirPath).then(() => {
50. console.info('remove file succeed');
51. }).catch((err: Error) => {
52. console.error('remove file failed with error message: ' + err.message);
53. });
54. }
55. }

57. })
58. }

60. build() {
61. Column() {
62. Button('Write data to cache')
63. .onClick(() => {
64. this.writeFile();
65. })
66. Button('Get the system cache size')
67. .onClick(() => {
68. this.getCache();
69. })
70. Button('Click to clear cache')
71. .onClick(() => {
72. this.clearCache();
73. })
74. }
75. }
76. }
```

[CacheSizeAndCleanupAPI.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CoreFileKit/entry/src/main/ets/pages/CacheSizeAndCleanupAPI.ets#L21-L96)
