---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-contacts-3
title: 使用ContactsKit中的selectContacts方法报错
breadcrumb: FAQ > 应用服务开发 > 联系人服务（Contacts Kit） > 使用ContactsKit中的selectContacts方法报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ebcf8f41c648f592e69ece8d45b6079e31d4a8fc77027892c372a86b554908b4
---

## 问题现象

使用ContactsKit中的selectContacts方法打开选择联系人UI界面，传入筛选条件（filterClause），执行过程中抛出401错误。导致联系人选择器无法正常显示，无法进行联系人选择操作。

## 背景知识

* [contact.selectContacts](../harmonyos-references/js-apis-contact.md#contactselectcontacts10-2)：用于在应用中弹出联系人选择器的方法，允许用户从系统联系人中选择若干个联系人。
* [ContactSelectionOptions](../harmonyos-references/js-apis-contact.md#contactselectionoptions10)：用于配置选择联系人条件。
* [ContactSelectionFilter](../harmonyos-references/js-apis-contact.md#contactselectionfilter15)：用于配置联系人查询过滤条件。

## 问题定位

通过分析代码发现，在调用selectContacts方法时，filterClause的参数使用for循环传入了多个filterCondition一样的id，不符合接口预期，从而返回401错误。

```ts
let arr: contact.FilterOptions[] = []
for (const id of ['1','2','3','4']) {
  arr.push({filterCondition:contact.FilterCondition.IN, value:id})
}

contact.selectContacts({
  isMultiSelect: true,
  maxSelectable: 4,
  filter: {
    filterType:contact.FilterType.DEFAULT_SELECT,
    filterClause:{id:arr}
  },
},(err: BusinessError, data) => {
  if (err) {
    console.error(`selectContact callback, errCode:${err.code}, errMessage:${err.message}`);
    return;
  }
  console.info(`selectContact callback: success data->${JSON.stringify(data)}`);
});
```

## 分析结论

问题根因是filterClause传入参数错误。

## 修改建议

若filterCondition一致，无需传入多个id值。

```ts
import { contact } from '@kit.ContactsKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SelectContacts {
  build() {
    Column(){
      Button('选择联系人')
        .width(100)
        .height(50)
        .margin({top:200})
        .onClick(()=>{
          contact.selectContacts({
            isMultiSelect: true,
            maxSelectable: 4,
            filter: {
              filterType:contact.FilterType.DEFAULT_SELECT,
              filterClause:{id:[{filterCondition:contact.FilterCondition.IN, value:['1','2','3','4']}]}
            },
          },(err: BusinessError, data) => {
            if (err) {
              console.error(`selectContact callback, errCode:${err.code}, errMessage:${err.message}`);
              return;
            }
            console.info(`selectContact callback: success data->${JSON.stringify(data)}`);
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
