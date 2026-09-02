---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-contacts-2
title: 调用queryContactsByPhoneNumber接口异常怎么解决
breadcrumb: FAQ > 应用服务开发 > 联系人服务（Contacts Kit） > 调用queryContactsByPhoneNumber接口异常怎么解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ac672c5f98fc09a72672506a06e3d505bd04e41bf005dc3034987bdd48763190
---

## 问题现象

开发者在使用Contacts Kit开发联系人相关功能时会遇到以下常见问题：

* 参照官方文档在AGC中已经配置了通讯录读写权限，工程中也配置了通讯录读权限，但是在启动调试或运行应用/服务时，安装HAP出现错误，提示：

  ```screen
  error: install failed due to grant request permissions failed
  ```
* 根据电话号码使用contact.queryContactsByPhoneNumber查出来的联系人缺少name信息。

## 背景知识

Contacts Kit可以帮助开发者轻松实现联系人的增删改查等功能。该Kit提供了一系列API，可以让开发者在应用中快速集成联系人管理功能，详情请参考[@ohos.contact API](../harmonyos-references/js-apis-contact.md)。

## 问题定位

1. 检查ACL受限权限是否申请成功，生成Profile时是否进行勾选对应受限权限。然后检查手动签名是否更新了Profile文件等签名信息。
2. 检查接口使用是否正确，接口返回值是否有name字段。

## 分析结论

1. ohos.permission.READ\_CONTACTS是受限开放权限，授权方式是用户授权（user\_grant）。该问题是由于默认应用等级为normal，只能使用normal等级的权限，如果使用了system\_basic、system\_core等级或受限开放的权限，将导致报错。
2. [contact.queryContactsByPhoneNumber](../harmonyos-references/js-apis-contact.md#contactquerycontactsbyphonenumber10-2)接口仅返回联系人信息中的id、key、phoneNumbers属性。
   * 如果要查询联系人的所有信息，建议使用[contact.queryContact](../harmonyos-references/js-apis-contact.md#contactquerycontact10-3)接口，根据contact.queryContactsByPhoneNumber接口返回的属性key查询。
   * contact.queryContact有多个入参不同的同名接口，详情参考[@ohos.contact API](../harmonyos-references/js-apis-contact.md)。其中入参含有attrs联系人的属性列表的接口需要注意，attrs不传默认查询所有联系人属性，如果传了就需要包含contact.Attribute.ATTR\_NAME接口才会返回name。

## 修改建议

查询联系人信息有两种方式，一种是使用Picker选择联系人获取信息，另一种是使用[@ohos.contact API](../harmonyos-references/js-apis-contact.md)查询联系人信息：

* 使用Picker选择联系人：

  通过Picker的方式，拉起联系人列表，引导用户完成界面操作，接口本身无需申请权限，因此推荐使用这种方式。

  ```screen
  // 1.调用联系人接口，拉起联系人列表，用户点击对应的联系人后返回
  if (canIUse('SystemCapability.Applications.Contacts')) {
    contact.selectContacts({
      isMultiSelect: false
    }, (err: BusinessError, data) => {
      if (err) {
        console.error('selectContact callback, errCode:' + err.code + ', errMessage:' + err.message);
        return;
      }
      // 2.完成操作，返回想要的data数据
      console.info(`selectContact callback: success data->${JSON.stringify(data)}`);
    });
  } else {
    console.error('The current device does not support contact queries.');
  }
  ```
* 使用[@ohos.contact API](../harmonyos-references/js-apis-contact.md)查询联系人信息：
  + Contacts Kit当前能力受限开放，需要申请受限开放权限ohos.permission.READ\_CONTACTS或ohos.permission.WRITE\_CONTACTS。该权限通常不允许三方应用申请，仅符合指定场景的应用可申请该权限。
    - 申请方式请参考：[申请使用受限权限](../harmonyos-guides/declare-permissions-in-acl.md)。
    - ACL提权参考：[申请ACL权限](../app/agc-help-apply-acl-0000002394212138.md)。
  + 使用[@ohos.contact API](../harmonyos-references/js-apis-contact.md)查询联系人信息：此方式需要关注使用的接口的入参是否含有attrs联系人的属性列表。以contact.queryContact接口为例，attrs不传默认查询所有联系人属性，如果传了就需要包含contact.Attribute.ATTR\_NAME接口才会返回name。

    ```screen
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const permissions: Array<Permissions> = ['ohos.permission.READ_CONTACTS'];
    abilityAccessCtrl.createAtManager()
      .requestPermissionsFromUser(context, permissions)
      .then((result: PermissionRequestResult) => {
        if (result.authResults[0] !== 0) { // 0 表示请求权限成功，其他任何非零值表示请求失败
          console.error('request contact permissions failed');
          return;
        }
        if (canIUse('SystemCapability.Applications.ContactsData')) {
          contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
            attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
          }, (err: BusinessError, data) => {
            if (err) {
              console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
              return;
            }
            console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
            if (data.length !== 0) {
              contact.queryContact(context, data[0].key, {
                attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
              }, (err: BusinessError, data) => {
                if (err) {
                  console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
                  return;
                }
                console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
              });
            }
          });
        } else {
          console.error('The current device does not support contact queries.');
        }
      })
      .catch((err: BusinessError) => {
        console.error(`Failed to queryContactsByPhoneNumber. Code: ${err.code}, message: ${err.message}`);
      });
    ```

完整示例参考如下：

```screen
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';
import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';

@Entry
@Component
struct ContactExample {
  build() {
    Column({ space: 20 }) {
      Button('使用Picker选择联系人')
        .onClick(() => {
          // 1.调用联系人接口，拉起联系人列表，用户点击对应的联系人后返回
          if (canIUse('SystemCapability.Applications.Contacts')) {
            contact.selectContacts({
              isMultiSelect: false
            }, (err: BusinessError, data) => {
              if (err) {
                console.error('selectContact callback, errCode:' + err.code + ', errMessage:' + err.message);
                return;
              }
              // 2.完成操作，返回想要的data数据
              console.info(`selectContact callback: success data->${JSON.stringify(data)}`);
            });
          } else {
            console.error('The current device does not support contact queries.');
          }
        });

      Button('根据电话号码和attrs查询联系人')
        .onClick(() => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          const permissions: Array<Permissions> = ['ohos.permission.READ_CONTACTS'];
          abilityAccessCtrl.createAtManager()
            .requestPermissionsFromUser(context, permissions)
            .then((result: PermissionRequestResult) => {
              if (result.authResults[0] !== 0) { // 0 表示请求权限成功，其他任何非零值表示请求失败
                console.error('request contact permissions failed');
                return;
              }
              if (canIUse('SystemCapability.Applications.ContactsData')) {
                contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
                  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
                }, (err: BusinessError, data) => {
                  if (err) {
                    console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
                    return;
                  }
                  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
                  if (data.length !== 0) {
                    contact.queryContact(context, data[0].key, {
                      attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
                    }, (err: BusinessError, data) => {
                      if (err) {
                        console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
                        return;
                      }
                      console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
                    });
                  }
                });
              } else {
                console.error('The current device does not support contact queries.');
              }
            })
            .catch((err: BusinessError) => {
              console.error(`Failed to queryContactsByPhoneNumber. Code: ${err.code}, message: ${err.message}`);
            });
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
