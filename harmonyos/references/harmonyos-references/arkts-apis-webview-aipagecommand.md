---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-aipagecommand
title: AIPageCommand
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > AIPageCommand
category: harmonyos-references
scraped_at: 2026-09-02T15:01:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4bb58b617638e223ff508e64f95bbfadf283869f6c9bb92578eae57420d5230f
---

AIPageCommand定义[executeAIPageCommand](arkts-apis-webview-webviewcontroller.md#executeaipagecommand)支持的JSON命令协议，包括不同命令的入参格式和返回格式。调用该接口前，应用需要将命令对象序列化为JSON字符串。

**说明** 

* command必须为JSON对象字符串。
* method字段取值区分大小写，需使用[命令总览](arkts-apis-webview-aipagecommand.md#命令总览)中列出的取值。
* 返回值非空时为JSON字符串，应用可通过JSON.parse解析后使用。
* 当网页不可用、命令无法执行或无结果返回时，接口返回空字符串。

## 命令总览

| method | 功能 | 入参格式 | 返回格式 | 说明 |
| --- | --- | --- | --- | --- |
| [getFullDom](arkts-apis-webview-aipagecommand.md#getfulldom) | 获取完整DOM树 | [FullDomCommand](arkts-apis-webview-aipagecommand.md#fulldomcommand) | [FullDomResult](arkts-apis-webview-aipagecommand.md#fulldomresult) | 返回树结构，不按筛选规则过滤节点。适用于需要完整层级结构的场景。 |
| [getLiteDom](arkts-apis-webview-aipagecommand.md#getlitedom) | 获取轻量DOM节点列表 | [LiteDomCommand](arkts-apis-webview-aipagecommand.md#litedomcommand) | [LiteDomResult](arkts-apis-webview-aipagecommand.md#litedomresult) | 返回扁平列表，支持按规则筛选节点。 |
| [screenCapture](arkts-apis-webview-aipagecommand.md#screencapture) | 获取网页元素截图 | [ScreenCaptureCommand](arkts-apis-webview-aipagecommand.md#screencapturecommand) | [ScreenCaptureResult](arkts-apis-webview-aipagecommand.md#screencaptureresult) | 返回Base64编码图片数据，支持获取当前网页视口截图或视口内目标元素截图。 |
| [getZoomLevel](arkts-apis-webview-aipagecommand.md#getzoomlevel) | 获取网页缩放比例 | [GetZoomLevelCommand](arkts-apis-webview-aipagecommand.md#getzoomlevelcommand) | [ZoomLevelResult](arkts-apis-webview-aipagecommand.md#zoomlevelresult) | 获取当前网页的缩放比例。 |

交互类命令请参见[AIPageInteraction](arkts-apis-webview-aipageinteraction.md)。

## 通用命令格式

| 参数 | 子参数 | 参数项 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| method | - | - | string | 是 | 命令名称。支持的取值请参见[命令总览](arkts-apis-webview-aipagecommand.md#命令总览)。 |
| params | - | - | Object | 否 | 命令参数。不同method对应的params格式不同。不传入时具体行为由各命令定义。 |

## getFullDom

获取当前网页的完整DOM树结构。该命令从文档根节点开始遍历，返回树形节点列表。

### FullDomCommand

```json
{
  "method": "getFullDom",
  "params": {
    "wants": [
      "rect",
      "visible",
      "xpath"
    ]
  }
}
```

### 入参说明

| 参数 | 子参数 | 参数项 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| method | - | - | string | 是 | 命令名称，固定为getFullDom。 |
| params | - | - | Object | 否 | 命令参数。不传入时使用默认返回字段。 |
| params | wants | - | Array<string> | 否 | 指定需要在节点中追加返回的字段。数组项表示节点信息字段，取值请参见[getFullDom的params.wants字段取值说明](arkts-apis-webview-aipagecommand.md#getfulldom的paramswants字段取值说明)。getFullDom会默认请求tag、text和全部HTML属性。 |

**说明** 

getFullDom默认返回当前网页的url、title和children\_nodes。children\_nodes中的节点默认返回tag、text、attributes和children\_nodes；其中text和attributes在字段值为空时不会返回。

### getFullDom的params.wants字段取值说明

| 取值 | 返回字段 | 返回类型 | 说明 |
| --- | --- | --- | --- |
| id | id | string | 请求返回ArkWeb生成的节点标识，不表示按HTML id属性筛选节点。该值由frame标识、文档作用域标识和DOM节点标识组合编码，用于区分返回结果中的节点；页面重新加载、frame重建或DOM重建后可能变化。仅在可生成节点标识时返回。如需读取HTML id属性，请查看返回节点的attributes.id。 |
| tag | tag | string | 节点标签名。元素节点返回小写HTML标签名，文本节点返回#text，ShadowRoot节点返回#shadowRoot。 |
| text | text | string | 节点文本内容。字段值为空时不返回该字段。 |
| title | title | string | 节点title属性值。字段值为空时不返回该字段。 |
| aria-label | aria-label | string | 节点aria-label属性值。字段值为空时不返回该字段。 |
| role | role | string | 节点语义角色。字段值为空时不返回该字段。 |
| aria-description | aria-description | string | 节点aria-description属性值。字段值为空时不返回该字段。 |
| rect | rect | Object | 节点矩形信息，包含x、y、width、height。 |
| bounds | bounds | Object | 节点矩形信息，包含x、y、left、top、right、bottom、width、height。 |
| visible | visible | boolean | 节点是否可见。true表示可见，false表示不可见。 |
| isInViewport | isInViewport | boolean | 节点是否在当前视口内。true表示在当前视口内，false表示不在当前视口内。 |
| clickable | clickable | boolean | 节点是否可点击。true表示可点击，false表示不可点击。 |
| touchable | touchable | boolean | 节点是否可触控。true表示可触控，false表示不可触控。当前判断逻辑与clickable一致。 |
| scrollable | scrollable | boolean | 节点是否可滚动。true表示可滚动，false表示不可滚动。 |
| inputable | inputable | boolean | 节点是否可输入。true表示可输入，false表示不可输入。 |
| url | url | string | 节点关联URL。按href、src、action、data、poster顺序读取并转换为完整URL。字段值为空时不返回该字段。 |
| xpath | xpath | string | 节点XPath。字段值为空时不返回该字段。 |
| hover | hover | string | 节点cursor样式值。字段值为空时不返回该字段。 |
| mouseover | mouseover | boolean | 节点是否声明mouseover内联事件。true表示已声明，false表示未声明。 |
| mouseenter | mouseenter | boolean | 节点是否声明mouseenter内联事件。true表示已声明，false表示未声明。 |
| value | value | string | 当节点为select元素时，返回当前选中值。 |
| options | options | Array<Object> | 当节点为select元素时，返回选项列表。 |
| value\_text | value\_text | Array<Object> | 当节点为select元素时，返回选项列表。 |
| focusable | focusable | boolean | 节点是否可获取焦点。true表示可获取焦点，false表示不可获取焦点。 |
| editable | editable | boolean | 节点是否可编辑。true表示可编辑，false表示不可编辑。 |
| settable | settable | boolean | 节点是否可设置值。true表示可设置值，false表示不可设置值。 |
| checked | checked | boolean | 节点是否处于选中状态。true表示处于选中状态，false表示不处于选中状态。 |
| expanded | expanded | boolean | 节点是否处于展开状态。true表示处于展开状态，false表示不处于展开状态。 |
| pressed | pressed | boolean | 节点是否处于按下状态。true表示处于按下状态，false表示不处于按下状态。 |
| selected | selected | boolean | 节点是否处于选择状态。true表示处于选择状态，false表示不处于选择状态。 |
| required | required | boolean | 节点是否为必填项。true表示为必填项，false表示为非必填项。 |
| autocomplete | autocomplete | string | 节点自动完成信息，优先读取aria-autocomplete属性，其次读取autocomplete属性。字段值为空时不返回该字段。 |
| keyshortcuts | keyshortcuts | string | 节点aria-keyshortcuts属性值。字段值为空时不返回该字段。 |

### FullDomResult

| 字段 | 子字段 | 字段项 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| url | - | - | string | 当前网页URL。 |
| title | - | - | string | 当前网页标题。 |
| children\_nodes | - | - | Array<Object> | DOM树根节点列表。 |
| children\_nodes | - | id | string | ArkWeb生成的节点标识，不是HTML id属性。仅在wants中包含id且可生成节点标识时返回。 |
| children\_nodes | - | tag | string | 节点标签名。 |
| children\_nodes | - | text | string | 节点文本内容。 |
| children\_nodes | - | title | string | 节点title属性值。 |
| children\_nodes | - | aria-label | string | 节点aria-label属性值。 |
| children\_nodes | - | role | string | 节点语义角色。 |
| children\_nodes | - | aria-description | string | 节点aria-description属性值。 |
| children\_nodes | - | rect | Object | 节点矩形信息。 |
| children\_nodes | rect | x | number | 节点矩形左上角x坐标。单位：px。 |
| children\_nodes | rect | y | number | 节点矩形左上角y坐标，相对于当前节点所属frame的视口左上角。单位：px。 |
| children\_nodes | rect | width | number | 节点矩形宽度。单位：px。 |
| children\_nodes | rect | height | number | 节点矩形高度。单位：px。 |
| children\_nodes | - | bounds | Object | 节点矩形信息。 |
| children\_nodes | bounds | x | number | 节点矩形左上角x坐标。单位：px。 |
| children\_nodes | bounds | y | number | 节点矩形左上角y坐标。单位：px。 |
| children\_nodes | bounds | left | number | 节点矩形左边界。单位：px。 |
| children\_nodes | bounds | top | number | 节点矩形上边界。单位：px。 |
| children\_nodes | bounds | right | number | 节点矩形右边界。单位：px。 |
| children\_nodes | bounds | bottom | number | 节点矩形下边界。单位：px。 |
| children\_nodes | bounds | width | number | 节点矩形宽度。单位：px。 |
| children\_nodes | bounds | height | number | 节点矩形高度。单位：px。 |
| children\_nodes | - | visible | boolean | 节点是否可见。true表示可见，false表示不可见。 |
| children\_nodes | - | isInViewport | boolean | 节点是否在当前视口内。true表示在当前视口内，false表示不在当前视口内。 |
| children\_nodes | - | clickable | boolean | 节点是否可点击。true表示可点击，false表示不可点击。 |
| children\_nodes | - | touchable | boolean | 节点是否可触控。true表示可触控，false表示不可触控。 |
| children\_nodes | - | scrollable | boolean | 节点是否可滚动。true表示可滚动，false表示不可滚动。 |
| children\_nodes | - | inputable | boolean | 节点是否可输入。true表示可输入，false表示不可输入。 |
| children\_nodes | - | url | string | 节点关联URL。 |
| children\_nodes | - | xpath | string | 节点XPath。 |
| children\_nodes | - | hover | string | 节点cursor样式值。 |
| children\_nodes | - | mouseover | boolean | 节点是否声明mouseover内联事件。true表示已声明，false表示未声明。 |
| children\_nodes | - | mouseenter | boolean | 节点是否声明mouseenter内联事件。true表示已声明，false表示未声明。 |
| children\_nodes | - | value | string | select元素当前选中值。 |
| children\_nodes | - | options | Array<Object> | select元素选项列表。 |
| children\_nodes | - | value\_text | Array<Object> | select元素选项列表。 |
| children\_nodes | options/value\_text | value | string | select元素选项值。 |
| children\_nodes | options/value\_text | text | string | select元素选项文本。 |
| children\_nodes | - | focusable | boolean | 节点是否可获取焦点。true表示可获取焦点，false表示不可获取焦点。 |
| children\_nodes | - | editable | boolean | 节点是否可编辑。true表示可编辑，false表示不可编辑。 |
| children\_nodes | - | settable | boolean | 节点是否可设置值。true表示可设置值，false表示不可设置值。 |
| children\_nodes | - | checked | boolean | 节点是否处于选中状态。true表示处于选中状态，false表示不处于选中状态。 |
| children\_nodes | - | expanded | boolean | 节点是否处于展开状态。true表示处于展开状态，false表示不处于展开状态。 |
| children\_nodes | - | pressed | boolean | 节点是否处于按下状态。true表示处于按下状态，false表示不处于按下状态。 |
| children\_nodes | - | selected | boolean | 节点是否处于选择状态。true表示处于选择状态，false表示不处于选择状态。 |
| children\_nodes | - | required | boolean | 节点是否为必填项。true表示为必填项，false表示为非必填项。 |
| children\_nodes | - | autocomplete | string | 节点自动完成信息。 |
| children\_nodes | - | keyshortcuts | string | 节点aria-keyshortcuts属性值。 |
| children\_nodes | - | attributes | Object | HTML属性集合。 |
| children\_nodes | attributes | <attributeName> | string | HTML属性名及对应属性值。 |
| children\_nodes | - | children\_nodes | Array<Object> | 当前节点的子节点列表。 |

**说明** 

* children\_nodes中的节点字段由默认字段和wants共同决定。字段值为空时，部分字符串字段和attributes字段不会返回。
* getFullDom会跳过script、noscript、style、template和slot元素子树。
* getFullDom会遍历开放或关闭的作者Shadow DOM，不返回用户代理Shadow DOM。
* 对于可解析的子frame，子frame根节点会合并到对应frame owner节点的children\_nodes中。

### 请求示例

```json
{
  "method": "getFullDom",
  "params": {
    "wants": [
      "rect",
      "visible",
      "xpath"
    ]
  }
}
```

### 返回示例

```json
{
  "url": "https://www.example.com/",
  "title": "Example",
  "children_nodes": [
    {
      "tag": "html",
      "attributes": {
        "lang": "en"
      },
      "rect": {
        "x": 0,
        "y": 0,
        "width": 360,
        "height": 640
      },
      "visible": true,
      "xpath": "/html[1]",
      "children_nodes": [
        {
          "tag": "body",
          "children_nodes": [
            {
              "tag": "button",
              "attributes": {
                "id": "submit"
              },
              "rect": {
                "x": 24,
                "y": 36,
                "width": 96,
                "height": 40
              },
              "visible": true,
              "xpath": "/html[1]/body[1]/button[1]",
              "children_nodes": [
                {
                  "tag": "#text",
                  "text": "Submit",
                  "children_nodes": []
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## getLiteDom

获取当前网页的轻量DOM节点列表。该命令会先根据rules筛选节点，再根据wants返回指定字段。

### LiteDomCommand

```json
{
  "method": "getLiteDom",
  "params": {
    "rules": {
      "tags": ["button", "a"],
      "isInViewport": true
    },
    "wants": [
      "id",
      "tag",
      "text",
      "rect",
      "clickable",
      "xpath",
      {
        "attributes": ["id", "class", "href"]
      }
    ]
  }
}
```

### 入参说明

| 参数 | 子参数 | 参数项 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| method | - | - | string | 是 | 命令名称，固定为getLiteDom。 |
| params | - | - | Object | 否 | 命令参数。不传入时不按规则筛选节点，并使用默认返回字段。 |
| params | rules | - | Object | 否 | 节点筛选规则。不传入时返回所有未被跳过的元素节点。 |
| params | rules | tags | Array<string> | 否 | 按HTML标签名称筛选节点。当需要筛选特定类型的HTML元素时使用（如只获取按钮或链接），不传此条件时不按标签筛选。 |
| params | rules | attributes | Array<string> | Object | 否 | 按HTML属性筛选节点。传入Array时，判断节点是否包含指定属性；传入Object时，key表示属性名，value为非空字符串时表示属性值需要包含该字符串。 |
| params | rules | roles | Array<string> | 否 | 按节点语义角色筛选节点。 |
| params | rules | clickable | boolean | 否 | 按节点是否可点击筛选。true表示筛选可点击的节点，false表示筛选不可点击的节点。 |
| params | rules | scrollable | boolean | 否 | 按节点是否可滚动筛选。true表示筛选可滚动的节点，false表示筛选不可滚动的节点。 |
| params | rules | isInViewport | boolean | 否 | 按节点是否在当前视口内筛选。true表示筛选在当前视口内的节点，false表示筛选不在当前视口内的节点。 |
| params | wants | - | Array<string | Object> | 否 | 指定需要在节点中追加返回的字段。getLiteDom会默认请求tag、text和xpath。 |
| params | wants | - | string | 否 | 数组项为string时，表示需要追加返回的节点信息字段，取值请参见[getLiteDom的params.wants字段取值说明](arkts-apis-webview-aipagecommand.md#getlitedom的paramswants字段取值说明)。 |
| params | wants | attributes | Array<string> | 否 | 数组项为Object且包含attributes时，指定需要返回的HTML属性。 |

**说明** 

* getLiteDom默认返回当前网页的url、title和nodes。nodes中的节点默认返回tag、text和xpath；其中text在字段值为空时不会返回。
* isInViewport会与其他筛选规则叠加生效。
* tags、attributes、roles、clickable和scrollable之间满足任一规则即可匹配。
* 如果未设置tags、attributes、roles、clickable和scrollable，则所有未被跳过的元素节点均满足筛选条件。

### getLiteDom的params.wants字段取值说明

| 取值 | 返回字段 | 返回类型 | 说明 |
| --- | --- | --- | --- |
| id | id | string | 请求返回ArkWeb生成的节点标识，不表示按HTML id属性筛选节点。该值由frame标识、文档作用域标识和DOM节点标识组合编码，用于区分返回结果中的节点；页面重新加载、frame重建或DOM重建后可能变化。仅在可生成节点标识时返回。如需读取HTML id属性，请在wants中通过attributes对象项请求id属性，并查看返回节点的attributes.id。 |
| tag | tag | string | 节点标签名。返回小写HTML标签名。 |
| text | text | string | 节点文本内容。字段值为空时不返回该字段。 |
| title | title | string | 节点title属性值。字段值为空时不返回该字段。 |
| aria-label | aria-label | string | 节点aria-label属性值。字段值为空时不返回该字段。 |
| role | role | string | 节点语义角色。字段值为空时不返回该字段。 |
| aria-description | aria-description | string | 节点aria-description属性值。字段值为空时不返回该字段。 |
| rect | rect | Object | 节点矩形信息，包含x、y、width、height。 |
| bounds | bounds | Object | 节点矩形信息，包含x、y、left、top、right、bottom、width、height。 |
| visible | visible | boolean | 节点是否可见。true表示可见，false表示不可见。 |
| isInViewport | isInViewport | boolean | 节点是否在当前视口内。true表示在当前视口内，false表示不在当前视口内。 |
| clickable | clickable | boolean | 节点是否可点击。true表示可点击，false表示不可点击。 |
| touchable | touchable | boolean | 节点是否可触控。true表示可触控，false表示不可触控。当前判断逻辑与clickable一致。 |
| scrollable | scrollable | boolean | 节点是否可滚动。true表示可滚动，false表示不可滚动。 |
| inputable | inputable | boolean | 节点是否可输入。true表示可输入，false表示不可输入。 |
| url | url | string | 节点关联URL。按href、src、action、data、poster顺序读取并转换为完整URL。字段值为空时不返回该字段。 |
| xpath | xpath | string | 节点XPath。字段值为空时不返回该字段。 |
| hover | hover | string | 节点cursor样式值。字段值为空时不返回该字段。 |
| mouseover | mouseover | boolean | 节点是否声明mouseover内联事件。true表示已声明，false表示未声明。 |
| mouseenter | mouseenter | boolean | 节点是否声明mouseenter内联事件。true表示已声明，false表示未声明。 |
| value | value | string | 当节点为select元素时，返回当前选中值。 |
| options | options | Array<Object> | 当节点为select元素时，返回选项列表。 |
| value\_text | value\_text | Array<Object> | 当节点为select元素时，返回选项列表。 |
| focusable | focusable | boolean | 节点是否可获取焦点。true表示可获取焦点，false表示不可获取焦点。 |
| editable | editable | boolean | 节点是否可编辑。true表示可编辑，false表示不可编辑。 |
| settable | settable | boolean | 节点是否可设置值。true表示可设置值，false表示不可设置值。 |
| checked | checked | boolean | 节点是否处于选中状态。true表示处于选中状态，false表示不处于选中状态。 |
| expanded | expanded | boolean | 节点是否处于展开状态。true表示处于展开状态，false表示不处于展开状态。 |
| pressed | pressed | boolean | 节点是否处于按下状态。true表示处于按下状态，false表示不处于按下状态。 |
| selected | selected | boolean | 节点是否处于选择状态。true表示处于选择状态，false表示不处于选择状态。 |
| required | required | boolean | 节点是否为必填项。true表示为必填项，false表示为非必填项。 |
| autocomplete | autocomplete | string | 节点自动完成信息，优先读取aria-autocomplete属性，其次读取autocomplete属性。字段值为空时不返回该字段。 |
| keyshortcuts | keyshortcuts | string | 节点aria-keyshortcuts属性值。字段值为空时不返回该字段。 |

### LiteDomResult

| 字段 | 子字段 | 字段项 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| url | - | - | string | 当前网页URL。 |
| title | - | - | string | 当前网页标题。 |
| nodes | - | - | Array<Object> | 符合筛选规则的节点列表。 |
| nodes | - | id | string | ArkWeb生成的节点标识，不是HTML id属性。仅在wants中包含id且可生成节点标识时返回。 |
| nodes | - | tag | string | 节点标签名。 |
| nodes | - | text | string | 节点文本内容。 |
| nodes | - | title | string | 节点title属性值。 |
| nodes | - | aria-label | string | 节点aria-label属性值。 |
| nodes | - | role | string | 节点语义角色。 |
| nodes | - | aria-description | string | 节点aria-description属性值。 |
| nodes | - | rect | Object | 节点矩形信息。 |
| nodes | rect | x | number | 节点矩形左上角x坐标。单位：px。 |
| nodes | rect | y | number | 节点矩形左上角y坐标，相对于当前节点所属frame的视口左上角。单位：px。 |
| nodes | rect | width | number | 节点矩形宽度。单位：px。 |
| nodes | rect | height | number | 节点矩形高度。单位：px。 |
| nodes | - | bounds | Object | 节点矩形信息。 |
| nodes | bounds | x | number | 节点矩形左上角x坐标。单位：px。 |
| nodes | bounds | y | number | 节点矩形左上角y坐标。单位：px。 |
| nodes | bounds | left | number | 节点矩形左边界。单位：px。 |
| nodes | bounds | top | number | 节点矩形上边界。单位：px。 |
| nodes | bounds | right | number | 节点矩形右边界。单位：px。 |
| nodes | bounds | bottom | number | 节点矩形下边界。单位：px。 |
| nodes | bounds | width | number | 节点矩形宽度。单位：px。 |
| nodes | bounds | height | number | 节点矩形高度。单位：px。 |
| nodes | - | visible | boolean | 节点是否可见。true表示可见，false表示不可见。 |
| nodes | - | isInViewport | boolean | 节点是否在当前视口内。true表示在当前视口内，false表示不在当前视口内。 |
| nodes | - | clickable | boolean | 节点是否可点击。true表示可点击，false表示不可点击。 |
| nodes | - | touchable | boolean | 节点是否可触控。true表示可触控，false表示不可触控。 |
| nodes | - | scrollable | boolean | 节点是否可滚动。true表示可滚动，false表示不可滚动。 |
| nodes | - | inputable | boolean | 节点是否可输入。true表示可输入，false表示不可输入。 |
| nodes | - | url | string | 节点关联URL。 |
| nodes | - | xpath | string | 节点XPath。 |
| nodes | - | hover | string | 节点cursor样式值。 |
| nodes | - | mouseover | boolean | 节点是否声明mouseover内联事件。true表示已声明，false表示未声明。 |
| nodes | - | mouseenter | boolean | 节点是否声明mouseenter内联事件。true表示已声明，false表示未声明。 |
| nodes | - | value | string | select元素当前选中值。 |
| nodes | - | options | Array<Object> | select元素选项列表。 |
| nodes | - | value\_text | Array<Object> | select元素选项列表。 |
| nodes | options/value\_text | value | string | select元素选项值。 |
| nodes | options/value\_text | text | string | select元素选项文本。 |
| nodes | - | focusable | boolean | 节点是否可获取焦点。true表示可获取焦点，false表示不可获取焦点。 |
| nodes | - | editable | boolean | 节点是否可编辑。true表示可编辑，false表示不可编辑。 |
| nodes | - | settable | boolean | 节点是否可设置值。true表示可设置值，false表示不可设置值。 |
| nodes | - | checked | boolean | 节点是否处于选中状态。true表示处于选中状态，false表示不处于选中状态。 |
| nodes | - | expanded | boolean | 节点是否处于展开状态。true表示处于展开状态，false表示不处于展开状态。 |
| nodes | - | pressed | boolean | 节点是否处于按下状态。true表示处于按下状态，false表示不处于按下状态。 |
| nodes | - | selected | boolean | 节点是否处于选择状态。true表示处于选择状态，false表示不处于选择状态。 |
| nodes | - | required | boolean | 节点是否为必填项。true表示为必填项，false表示为非必填项。 |
| nodes | - | autocomplete | string | 节点自动完成信息。 |
| nodes | - | keyshortcuts | string | 节点aria-keyshortcuts属性值。 |
| nodes | - | attributes | Object | HTML属性集合。 |
| nodes | attributes | <attributeName> | string | HTML属性名及对应属性值。 |

**说明** 

* nodes中的节点字段由默认字段和wants共同决定。字段值为空时，部分字符串字段和attributes字段不会返回。
* getLiteDom只返回元素节点，不返回文本节点。
* getLiteDom会跳过script、noscript、style、template和slot元素子树。
* getLiteDom会遍历开放或关闭的作者Shadow DOM，不返回用户代理Shadow DOM。
* 结果包含可解析子frame中的节点。节点在每个frame内保持DOM遍历顺序，子frame节点会整体追加到当前frame节点列表之后；多个子frame的合并顺序由内部frame token集合决定。

### 请求示例

```json
{
  "method": "getLiteDom",
  "params": {
    "rules": {
      "tags": ["button", "a"],
      "isInViewport": true
    },
    "wants": [
      "id",
      "tag",
      "text",
      "rect",
      "clickable",
      "xpath",
      {
        "attributes": ["id", "class", "href"]
      }
    ]
  }
}
```

### 返回示例

```json
{
  "url": "https://www.example.com/",
  "title": "Example",
  "nodes": [
    {
      "id": "frameToken|documentToken|12",
      "tag": "button",
      "rect": {
        "x": 24,
        "y": 36,
        "width": 96,
        "height": 40
      },
      "clickable": true,
      "xpath": "/html[1]/body[1]/button[1]",
      "attributes": {
        "id": "submit",
        "class": "primary"
      }
    }
  ]
}
```

## screenCapture

获取当前网页视口截图或视口内目标元素截图，返回Base64编码的图片数据。

### ScreenCaptureCommand

### 入参说明

| 参数 | 子参数 | 参数项 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| method | - | - | string | 是 | 命令名称，固定为screenCapture。 |
| params | - | - | Object | 否 | 命令参数。不传或为空时获取当前网页视口截图。 |
| params | nodeid | - | string | 否 | 目标元素的节点标识，可通过[getFullDom](arkts-apis-webview-aipagecommand.md#getfulldom)或[getLiteDom](arkts-apis-webview-aipagecommand.md#getlitedom)返回的id字段获取。 |
| params | xpath | - | string | 否 | 目标元素的XPath，可通过[getFullDom](arkts-apis-webview-aipagecommand.md#getfulldom)或[getLiteDom](arkts-apis-webview-aipagecommand.md#getlitedom)返回的xpath字段获取。 |

**说明** 

* nodeid与xpath互斥，均传入时以nodeid为准。两者均未传入时，默认获取当前网页视口截图。
* 支持获取iframe元素截图，不支持跨域获取iframe内部元素截图；不支持获取同层渲染ArkUI组件的截图。

### ScreenCaptureResult

成功时返回PNG格式的Base64编码字符串。

**说明** 

* nodeid格式错误，返回{"code": 392, "message": "invalid param: nodeid"}；nodeid中的frameToken或documentToken与当前页面不匹配，返回{"code": 392, "message": "invalid param: nodeid, token mismatch"}。
* 根据nodeid或xpath在页面中未找到目标元素，返回{"code": 352, "message": "element not found"}。

### 示例

通过节点标识获取目标元素截图：

```json
{
  "method": "screenCapture",
  "params": {
    "nodeid": "frameToken|documentToken|12"
  }
}
```

通过XPath获取目标元素截图：

```json
{
  "method": "screenCapture",
  "params": {
    "xpath": "/html/body/div/p[2]/a"
  }
}
```

**说明** 

* 开发者使用时需自行替换nodeid或xpath，可通过[getFullDom](arkts-apis-webview-aipagecommand.md#getfulldom)或[getLiteDom](arkts-apis-webview-aipagecommand.md#getlitedom)返回的id字段或xpath字段获取。

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

interface CaptureParams {
  xpath?: string;
  nodeid?: string;
}

interface PageCommand {
  method: string;
  params?: CaptureParams;
}

@Entry
@Component
struct Index {
  private controller: webview.WebviewController = new webview.WebviewController();
  @State imgData: string = '';
  @State statusMsg: string = '';

  async capture() {
    this.imgData = '';
    this.statusMsg = '';

    try {
      const cmd: PageCommand = {
        method: 'screenCapture',
        params: {
          xpath: "/html/body/div/p[2]/a"
        }
      };

      const res = await this.controller.executeAIPageCommand(JSON.stringify(cmd)) as string;

      if (res.includes('"code"')) {
        this.statusMsg = `截图失败：${res} `;
        return;
      }

      this.imgData = res;
      this.statusMsg = '✅ 截图成功';
    } catch (e) {
      const error = e as BusinessError;
      this.statusMsg = `截图失败：${error.message}`;
    }
  }

  build() {
    Row() {
      Web({ src: 'https://www.example.com', controller: this.controller })
        .width('75%')
        .height('100%')

      Column({ space: 10 }) {
        Button('执行截图')
          .width('100%')
          .onClick(() => this.capture())

        Image(this.imgData ? `data:image/png;base64,${this.imgData}` : '')
          .width('100%')
          .aspectRatio(1)
          .backgroundColor('#F0F0F0')
          .objectFit(ImageFit.Contain)
          .border({ width: 1, color: '#DCDCDC' })

        if (this.statusMsg) {
          Text(this.statusMsg)
            .width('100%')
            .fontSize(12)
            .fontColor(this.statusMsg.includes('✅') ? '#4CAF50' : '#F44336')
            .textAlign(TextAlign.Center)
            .padding(8)
            .backgroundColor(this.statusMsg.includes('✅') ? '#E8F5E9' : '#FFEBEE')
            .borderRadius(4)
        }
      }
      .width('25%')
      .padding(10)
      .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```

## getZoomLevel

获取当前网页的缩放比例。该命令为纯查询操作，不受[zoomControlAccess](arkts-basic-components-web-attributes.md#zoomcontrolaccess22)限制。

### GetZoomLevelCommand

```json
{
  "method": "getZoomLevel",
  "params": {}
}
```

### 入参说明

| 参数 | 子参数 | 参数项 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| method | - | - | string | 是 | 命令名称，固定为getZoomLevel。 |
| params | - | - | Object | 否 | 命令参数。本命令不读取params内容，可传入空对象或不传入。 |

**说明** 

* 返回的zoomLevel字段为当前网页的缩放比例（1.0=100%），与[setZoomLevel](arkts-apis-webview-aipageinteraction.md#setzoomlevel)传入的语义一致。
* [setZoomLevel](arkts-apis-webview-aipageinteraction.md#setzoomlevel)设置任意合法值后通过本命令读取，返回值误差不超过0.001。
* 用户先通过CTRL+Wheel缩放，再调用本命令，返回用户当前缩放比例。

### ZoomLevelResult

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| code | number | 执行结果码。取值请参见[命令执行结果码说明](arkts-apis-webview-aipageresult.md#命令执行结果码说明)。 |
| message | string | 执行结果描述。成功时为"success"。 |
| zoomLevel | number | 当前网页缩放比例。成功时返回。 |

### 测试页面

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
  <body>
    <h1>Zoom Level Demo</h1>
    <p>当前缩放比例可通过getZoomLevel查询，通过setZoomLevel（详见AIPageInteraction）修改。</p>
  </body>
</html>
```

### 请求示例

```json
{
  "method": "getZoomLevel",
  "params": {}
}
```

### 返回示例

成功时（页面当前缩放比例为1.5）：

```json
{
  "code": 10,
  "message": "success",
  "zoomLevel": 1.5
}
```

失败：

132（browser或host为空，通常表示Web实例不可用）：

```json
{
  "code": 132,
  "message": "browser or host is null"
}
```
