---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-configuration
title: "@system.configuration (应用配置)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > @system.configuration (应用配置)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d409c16d2adc339f8502cab7df8398a90dd4777b78a157c090137581decaed63
---

**说明** 

* 从API Version 7 开始，该接口不再维护，推荐使用新接口[@ohos.i18n](js-apis-i18n.md)和[@ohos.intl](js-apis-intl.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import Configuration from '@system.configuration';
```

## configuration.getLocale

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

```js
export default {
  getLocale() {
    const localeInfo = Configuration.getLocale();
    console.info(localeInfo.language);
  }
}
```

JS示例：

```xml
<!-- xxx.hml -->
<div class="container">
    <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
        configuration.getLocale example
    </text>
    <div class="section">
        <text class="section-title">Language Settings:</text>
        <div class="info-item">
            <text class="value">{{language}}</text>
        </div>
    </div>
    <div class="section">
        <text class="section-title">Region Settings:</text>
        <div class="info-item">
            <text class="value">{{countryOrRegion}}</text>
        </div>
    </div>
    <div class="section">
        <text class="section-title">Layout direction:</text>
        <div class="info-item">
            <text class="value">{{dir}}</text>
        </div>
    </div>
    <input type="button" value="Refresh configuration" style="width: 350px; height: 50px; margin: 5px;" onclick="getLocaleInfo"></input>
</div>
```

```css
/* xxx.css */
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    left: 0px;
    top: 0px;
    width: 454px;
    height: 454px;
    background-color: #000000;
}
.title {
    font-size: 24px;
    text-align: center;
    width: 320px;
    height: 100px;
    margin-top: 40px;
    color: #ffffff;
}
.section {
    width: 400px;
    height: 60px;
    padding: 15px;
    background-color: #1a1a1a;
    border-radius: 10px;
}
.section-title {
    font-size: 24px;
    color: #007dff;
    height: 35px;
    margin-bottom: 10px;
}
.info-item {
    width: 100%;
    height: 35px;
}
.label {
    font-size: 24px;
    height: 40px;
    color: #aaaaaa;
}
.value {
    font-size: 24px;
    height: 40px;
    color: #ffffff;
}
```

```js
// xxx.js
import configuration from '@system.configuration';

export default {
    data: {
        fontSize: '28px',
        fontColor: '#ffffff',
        language: '',
        countryOrRegion: '',
        dir: '',
        displayLanguage: '',
        displayRegion: '',
        displayDir: ''
    },
    onInit() {
        this.getLocaleInfo();
    },
    getLocaleInfo() {
        try {
            const localeInfo = configuration.getLocale();
            console.info('configuration.getLocale success');
            console.info('language: ' + localeInfo.language);
            console.info('countryOrRegion: ' + localeInfo.countryOrRegion);
            console.info('dir: ' + localeInfo.dir);
            
            this.language = localeInfo.language || 'Unknown';
            this.countryOrRegion = localeInfo.countryOrRegion || 'Unknown';
            this.dir = localeInfo.dir || 'Unknown';
            
            this.displayLanguage = this.getDisplayLanguage(this.language);
            this.displayRegion = this.getDisplayRegion(this.countryOrRegion);
            this.displayDir = this.getDisplayDirection(this.dir);
        } catch (error) {
            console.error('configuration.getLocale failed: ' + error.message);
            this.language = 'Failed';
            this.countryOrRegion = 'Failed';
            this.dir = 'Failed';
            this.displayLanguage = 'Failed';
            this.displayRegion = 'Failed';
            this.displayDir = 'Failed';
        }
    },
    getDisplayLanguage(language) {
        const map = {
            'zh': 'Chinese',
            'en': 'English',
            'ja': 'Japanese',
            'ko': 'Korean'
        };
        return map[language] || language;
    },
    getDisplayRegion(region) {
        const map = {
            'CN': 'China',
            'US': 'United States',
            'JP': 'Japan',
            'KR': 'South Korea'
        };
        return map[region] || region;
    },
    getDisplayDirection(dir) {
        if (dir === 'ltr') {
            return 'Left to Right';
        } else if (dir === 'rtl') {
            return 'Right to Left';
        }
        return dir;
    }
}
```

## LocaleResponse

表示应用当前Locale的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Lite

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| language | string | 是 | 否 | 语言。例如：zh。 |
| countryOrRegion | string | 是 | 否 | 国家或地区。例如：CN。 |
| dir | string | 是 | 否 | 文字布局方向。取值范围：  - ltr：从左到右。  - rtl：从右到左。 |
