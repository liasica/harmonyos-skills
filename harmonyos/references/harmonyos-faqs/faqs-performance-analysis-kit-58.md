---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-58
title: 使用HiLog打印日志是否有长度限制
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 使用HiLog打印日志是否有长度限制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f8e2e4b7dbf2fcc9c1c922048a5ba671f3120147d1b61aae1f5140f29dc2668a
---

使用HiLog进行日志打印时，最多支持4096字节，超出部分将被截断。

利用HiLog封装日志打印工具类，解决日志信息过长的问题。

示例如下：

封装LogUtil类：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. class LogUtil {
4. private static instance: LogUtil;
5. private static DOMAIN: number = 0x0000;

7. private constructor() {
8. // Private constructor to prevent external instantiation
9. }

11. public static getInstance(): LogUtil {
12. if (!LogUtil.instance) {
13. LogUtil.instance = new LogUtil();
14. }
15. return LogUtil.instance;
16. }

18. public logError(logTag: string, content: string) {
19. const maxSize = 1024;
20. if (content.length <= maxSize) {
21. // Length less than or equal to the limit for direct printing
22. } else {
23. while (content.length > maxSize) {
24. // Loop segmented printing
25. let logContent = content.substring(0, maxSize);
26. content = content.replace(logContent, '');
27. hilog.error(LogUtil.DOMAIN, logTag, '%{public}s', logContent);
28. // Print remaining logs
29. }
30. }
31. hilog.error(LogUtil.DOMAIN, logTag, '%{public}s', content);
32. }

34. public logDebug(logTag: string, content: string) {
35. const maxSize = 1024;
36. if (content.length <= maxSize) {
37. // Length less than or equal to the limit for direct printing
38. } else {
39. while (content.length > maxSize) {
40. //Loop segmented printing
41. let logContent = content.substring(0, maxSize);
42. content = content.replace(logContent, '');
43. hilog.debug(LogUtil.DOMAIN, logTag, '%{public}s', logContent);
44. // Print remaining logs
45. }
46. }
47. hilog.debug(LogUtil.DOMAIN, logTag, '%{public}s', content);
48. }

50. public logInfo(logTag: string, content: string) {
51. const maxSize = 1024;
52. if (content.length <= maxSize) {
53. // Length less than or equal to the limit for direct printing
54. } else {
55. while (content.length > maxSize) {
56. //Loop segmented printing
57. let logContent = content.substring(0, maxSize);
58. content = content.replace(logContent, '');
59. hilog.info(LogUtil.DOMAIN, logTag, '%{public}s', logContent);
60. // Print remaining logs
61. }
62. }
63. hilog.info(LogUtil.DOMAIN, logTag, '%{public}s', content);
64. }
65. }

67. export default LogUtil;
```

[LogUtilClass.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/pages/LogUtilClass.ets#L21-L87)

使用：

```
1. import LogUtil from './LogUtilClass';

3. @Entry
4. @Component
5. struct HiLogIsThereALengthLimit {
6. build() {
7. Row() {
8. Column() {
9. Button('hilog util')
10. .onClick(() => {
11. let str = 'Long log content';
12. let utilInfo = LogUtil.getInstance();
13. utilInfo.logInfo('testTag', str);
14. })
15. }
16. .width('100%')
17. }
18. .height('100%')
19. }
20. }
```

[HiLogIsThereALengthLimit.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/pages/HiLogIsThereALengthLimit.ets#L21-L40)
