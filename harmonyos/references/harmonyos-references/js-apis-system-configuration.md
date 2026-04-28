---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-configuration
title: @system.configuration (应用配置)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > @system.configuration (应用配置)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:51+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:66415f7000a89c263181d00b73ffcfb35feb0aab62d51a5b47d700c1eca4c436
---

说明

* 从API Version 7 开始，该接口不再维护，推荐使用新接口[@ohos.i18n](js-apis-i18n.md)和[@ohos.intl](js-apis-intl.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearableLite Wearable

```
1. import Configuration from '@system.configuration';
```

## configuration.getLocale

PhonePC/2in1TabletTVWearableLite Wearable

static getLocale(): LocaleResponse

获取应用当前的语言和地区。默认与系统的语言和地区同步。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| LocaleResponse | 应用当前Locale相关信息。 |

**示例：**

ArkTS示例：

```
1. export default {
2. getLocale() {
3. const localeInfo = configuration.getLocale();
4. console.info(localeInfo.language);
5. }
6. }
```

JS示例：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
4. configuration.getLocale example
5. </text>
6. <div class="section">
7. <text class="section-title">Language Settings:</text>
8. <div class="info-item">
9. <text class="value">{{language}}</text>
10. </div>
11. </div>
12. <div class="section">
13. <text class="section-title">Region Settings:</text>
14. <div class="info-item">
15. <text class="value">{{countryOrRegion}}</text>
16. </div>
17. </div>
18. <div class="section">
19. <text class="section-title">Layout direction:</text>
20. <div class="info-item">
21. <text class="value">{{dir}}</text>
22. </div>
23. </div>
24. <input type="button" value="Refresh configuration" style="width: 350px; height: 50px; margin: 5px;" onclick="getLocaleInfo"></input>
25. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. flex-direction: column;
5. align-items: center;
6. left: 0px;
7. top: 0px;
8. width: 454px;
9. height: 454px;
10. background-color: #000000;
11. }
12. .title {
13. font-size: 24px;
14. text-align: center;
15. width: 320px;
16. height: 100px;
17. margin-top: 40px;
18. color: #ffffff;
19. }
20. .section {
21. width: 400px;
22. height: 60px;
23. padding: 15px;
24. background-color: #1a1a1a;
25. border-radius: 10px;
26. }
27. .section-title {
28. font-size: 24px;
29. color: #007dff;
30. height: 35px;
31. margin-bottom: 10px;
32. }
33. .info-item {
34. width: 100%;
35. height: 35px;
36. }
37. .label {
38. font-size: 24px;
39. height: 40px;
40. color: #aaaaaa;
41. }
42. .value {
43. font-size: 24px;
44. height: 40px;
45. color: #ffffff;
46. }
```

```
1. // xxx.js
2. import configuration from '@system.configuration';

4. export default {
5. data: {
6. fontSize: '28px',
7. fontColor: '#ffffff',
8. language: '',
9. countryOrRegion: '',
10. dir: '',
11. displayLanguage: '',
12. displayRegion: '',
13. displayDir: ''
14. },
15. onInit() {
16. this.getLocaleInfo();
17. },
18. getLocaleInfo() {
19. try {
20. const localeInfo = configuration.getLocale();
21. console.info('configuration.getLocale success');
22. console.info('language: ' + localeInfo.language);
23. console.info('countryOrRegion: ' + localeInfo.countryOrRegion);
24. console.info('dir: ' + localeInfo.dir);

26. this.language = localeInfo.language || 'Unknown';
27. this.countryOrRegion = localeInfo.countryOrRegion || 'Unknown';
28. this.dir = localeInfo.dir || 'Unknown';

30. this.displayLanguage = this.getDisplayLanguage(this.language);
31. this.displayRegion = this.getDisplayRegion(this.countryOrRegion);
32. this.displayDir = this.getDisplayDirection(this.dir);
33. } catch (error) {
34. console.error('configuration.getLocale failed: ' + error.message);
35. this.language = 'Failed';
36. this.countryOrRegion = 'Failed';
37. this.dir = 'Failed';
38. this.displayLanguage = 'Failed';
39. this.displayRegion = 'Failed';
40. this.displayDir = 'Failed';
41. }
42. },
43. getDisplayLanguage(language) {
44. const map = {
45. 'zh': 'Chinese',
46. 'en': 'English',
47. 'ja': 'Japanese',
48. 'ko': 'Korean'
49. };
50. return map[language] || language;
51. },
52. getDisplayRegion(region) {
53. const map = {
54. 'CN': 'China',
55. 'US': 'United States',
56. 'JP': 'Japan',
57. 'KR': 'South Korea'
58. };
59. return map[region] || region;
60. },
61. getDisplayDirection(dir) {
62. if (dir === 'ltr') {
63. return 'Left to Right';
64. } else if (dir === 'rtl') {
65. return 'Right to Left';
66. }
67. return dir;
68. }
69. }
```

## LocaleResponse

PhonePC/2in1TabletTVWearableLite Wearable

表示应用当前Locale的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Lite

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| language | string | 是 | 否 | 语言。例如：zh。 |
| countryOrRegion | string | 是 | 否 | 国家或地区。例如：CN。 |
| dir | string | 是 | 否 | 文字布局方向。取值范围：  - ltr：从左到右。  - rtl：从右到左。 |
