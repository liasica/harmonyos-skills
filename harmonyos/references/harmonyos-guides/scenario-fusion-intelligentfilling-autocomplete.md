---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-intelligentfilling-autocomplete
title: 自动补全地址表单所在地区
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 自动补全地址表单所在地区
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:039977d9f0f5739d8d8486bedf3e676cb041dccf62fc805449eec1085d1b7754
---

在填写地址表单场景时，当应用使用了所在地区的省市区选择器，需要开发者对表单中的地址字段进行开发。

**说明** 

* 需要在module.json5文件中设置模糊位置权限：[ohos.permission.APPROXIMATELY\_LOCATION](permissions-for-all-user.md#ohospermissionapproximately_location)。
* 所在地区地址选择器需要[开通地图服务](map-config-agc.md#开通地图服务)。
* 需要[配置签名和指纹](account-sign-fingerprints.md)。

## 效果图

地址表单中的所在地区能根据详细地址内容自动补全，当补全内容不符合预期时，可通过地址选择器进行修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/ibbY5z5SQbO5nmjFtpC0Rw/zh-cn_image_0000002736434335.png)

## 示例代码

```typescript
import { util } from '@kit.ArkTS';
import { i18n } from '@kit.LocalizationKit';
import { sceneMap, site } from '@kit.MapKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';
import { abilityAccessCtrl, autoFillManager, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
import { TextInputModifier } from '@kit.ArkUI';

// 该权限已授权常量。
const AUTHED = 0;
// 延迟的毫秒数常量。
const TIME_OUT = 100;
// 默认纬度。以下以北京天安门的纬度为例。
const INIT_LAT = 39.5;
// 默认经度。以下以北京天安门的经度为例。
const INIT_LON = 116.2;
// 英语语言常量。
const ENGLISH = 'en';
// 简体中文常量。
const SIMPLIFIED_CHINESE = 'zh_CN';
// 应用获取设备模糊位置信息权限。
const PERMISSIONS: Permissions[] = ['ohos.permission.APPROXIMATELY_LOCATION'];
// 地址详细信息对应级别,根据业务需求动态配置需要显示的层级。
const ADMINISTRATIVE_REGION: string[] =
  ['countryName', 'adminLevel1', 'adminLevel2', 'adminLevel3', 'adminLevel4'];

interface PersonInfo {
  name?: string;
  phone?: string;
  email?: string;
  idCard?: string;
  region?: string;
  streetAddress?: string;
}

interface RequestParam {
  requestTag: string;
  requestText: string;
}

interface Location {
  latitude: number;
  longitude: number;
}

// 显示授权弹出窗口。
async function reqPermissionsFromUser(permissions: Array<Permissions>,
  context: common.UIAbilityContext): Promise<PermissionRequestResult> {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  return await atManager.requestPermissionsFromUser(context, permissions);
}

// 节流函数。
function debounce(func: () => void, wait: number = TIME_OUT): Function {
  let timeout: number | null = null;
  return () => {
    timeout && clearTimeout(timeout);
    timeout = setTimeout(() => {
      func();
      clearTimeout(timeout);
    }, wait);
  };
}

@Extend(Text)
function textStyle() {
  .width(64)
  .textAlign(TextAlign.End);
}

@Entry
@Component
struct Index {
  @State personInfo: PersonInfo = {};
  @State isClicked: boolean = false;
  // 用户是否已触发信息输入。
  private isUserInput: boolean = false;
  private location: Location = {
    latitude: INIT_LAT,
    longitude: INIT_LON
  };
  private currentRequestTag: string = '';
  private handleAddressChange = (request: RequestParam) => {
    return debounce(async () => {
      this.autoCompleteAddress(request);
    });
  };

  aboutToAppear() {
    reqPermissionsFromUser(PERMISSIONS, this.getUIContext().getHostContext() as common.UIAbilityContext)
      .then((permissionRequestResult: PermissionRequestResult) => {
        if (permissionRequestResult.authResults[0] === AUTHED) {
          // 获取位置信息的API只能在授权的情况下被调用。
          geoLocationManager.getCurrentLocation((err, location: geoLocationManager.Location) => {
            if (err) {
              hilog.error(0x0000, 'testTag', `Failed to get location, code: ${err?.code}, message: ${err?.message}`);
              return;
            }
            hilog.info(0x0000, 'testTag', `Succeeded in obtaining the current location of the user`);
            this.location.latitude = location.latitude;
            this.location.longitude = location.longitude;
          });
        }
      })
      .catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', `Failed request permissions, code: ${err?.code}, message: ${err?.message}`);
      });
  }

  public isUsLanguage(): boolean {
    let result: string = '';
    try {
      result = i18n.System.getSystemLanguage();
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'Failed to get system language');
    }
    return result.toLowerCase() === 'en-latn-us';
  }

  async autoCompleteAddress(request: RequestParam): Promise<void> {
    try {
      let params: site.SearchByTextParams = {
        query: request.requestText,
        // 搜索结果需要偏向的经纬度。
        location: {
          latitude: this.location.latitude,
          longitude: this.location.longitude
        },
        language: this.isUsLanguage() ? ENGLISH : SIMPLIFIED_CHINESE,
        isChildren: true
      };
      const result = await site.searchByText(params);
      if (result.sites) {
        let region: string = '';
        let addressComponent = result.sites[0].addressComponent;
        // 遍历当前地址的行政区划层级。
        for (let item of ADMINISTRATIVE_REGION) {
          if (addressComponent[item] === undefined) {
            break;
          }
          region += addressComponent[item];
        }
        // 防止可能导致结果不一致的重复搜索。
        if (request.requestTag === this.currentRequestTag) {
          this.personInfo.region = region;
        }
      }
    } catch (error) {
      hilog.error(0x0000, 'testTag', `Failed to search location, code: ${error.code}, message: ${error.message}`);
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in searching location');
  }

  onRegionClick(): void {
    // 用户选择行政区域后，仅显示该区域的搜索结果，以防止查询时间过长。
    this.currentRequestTag = util.generateRandomUUID();
    let districtSelectOptions: sceneMap.DistrictSelectOptions = {
      countryCode: 'CN'
    };
    sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
      hilog.info(0x0000, 'testTag', 'SelectDistrict', 'Succeeded  in selecting district.');
      let region = '';
      for (let i = 0; i < data?.districts?.length; i++) {
        region += data.districts[i].name;
      }
      this.personInfo.region = region;
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `Failed to select district, code: ${err.code}, message: ${err.message}`);
    });
  }

  searchRegionByAddress(val: string): void {
    let tag: string = util.generateRandomUUID();
    this.currentRequestTag = tag;
    let param: RequestParam = {
      requestTag: tag,
      requestText: val
    };
    // 用户输入的场景需要加做抖动处理，智能填充回填场景直接查询即可。
    if (this.personInfo.region && this.personInfo.region !== '') {
      return;
    }
    if (this.isUserInput) {
      this.handleAddressChange(param)();
    } else {
      this.autoCompleteAddress(param);
    }
  }

  build() {
// ...
      Column({ space: 8 }) {
        Row({ space: 8 }) {
          Text('姓名').textStyle()
          TextInput({ text: this.personInfo.name, placeholder: '姓名' })
            .layoutWeight(1)
            .contentType(ContentType.PERSON_FULL_NAME)
            .onChange((val: string) => {
              this.personInfo.name = val;
            })
        }

        Row({ space: 8 }) {
          Text('联系电话').textStyle()
          TextInput({ text: this.personInfo.phone, placeholder: '手机号码' })
            .layoutWeight(1)
            .contentType(ContentType.PHONE_NUMBER)
            .onChange((val: string) => {
              this.personInfo.phone = val;
            })
        }

        Row({ space: 8 }) {
          Text('身份证号').textStyle()
          TextInput({ text: this.personInfo.idCard, placeholder: '身份证信息' })
            .layoutWeight(1)
            .contentType(ContentType.ID_CARD_NUMBER)
            .onChange((val: string) => {
              this.personInfo.idCard = val;
            })
        }

        Row({ space: 8 }) {
          Text('邮件地址').textStyle()
          TextInput({ text: this.personInfo.email, placeholder: '电子邮件信息' })
            .layoutWeight(1)
            .contentType(ContentType.EMAIL_ADDRESS)
            .onChange((val: string) => {
              this.personInfo.email = val;
            })
        }

        Row({ space: 8 }) {
          Text('所在地区').textStyle()
          FunctionalInput({
            params: {
              // InputType.SELECT_DISTRICT表示输入类型为省/市/区选择器类型。
              inputType: functionalInputComponentManager.InputType.SELECT_DISTRICT,
              textInputValue: {
                text: this.personInfo.region,
                placeholder: '省、市、区、街道地址'
              },
              // 调整TextInput样式。
              inputAttributeModifier: new TextInputModifier()
                .backgroundColor(Color.Transparent)
                .onChange((value) => {
                  if (value !== this.personInfo.region) {
                    this.personInfo.region = value;
                  }
                })
            },
            // 当InputType为SELECT_DISTRICT时，回调必须为onSelectDistrict。
            controller: new functionalInputComponentManager.FunctionalInputController().onSelectDistrict((err,
              data: functionalInputComponentManager.DistrictSelectResult) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, 'testTag', 'Failed to select district, error: %{public}d %{public}s', err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, 'testTag', 'succeeded in selecting district');
              this.personInfo.region = data.inputContent;
            })
          })
        }

        Row({ space: 8 }) {
          Text('详细地址').textStyle()
          TextInput({ text: this.personInfo.streetAddress, placeholder: '小区门牌信息' })
            .layoutWeight(1)
            .contentType(ContentType.DETAIL_INFO_WITHOUT_STREET)
            .onDidInsert(() => {
              // 当用户通过输入方法输入数据时触发。
              this.isUserInput = true;
            })
            .onDidDelete((val: DeleteValue) => {
              // 当用户通过输入方法删除数据时触发。
              if (val?.deleteValue?.length > 0) {
                this.isUserInput = true;
              }
            })
            .onChange((val: string) => {
              this.personInfo.streetAddress = val;
              if (val && val.trim().length > 0) {
                this.searchRegionByAddress(val);
              } else {
                this.currentRequestTag = util.generateRandomUUID();
                this.personInfo.region = '';
              }
              this.isUserInput = false;
            })
        }

        Button('保存')
          .width('50%')
          .onClick(() => {
            if (!this.isClicked) {
              this.isClicked = true;
              autoFillManager.requestAutoSave(this.getUIContext(), {
                onSuccess: () => {
                  hilog.info(0x0000, 'testTag', 'Succeeded in saving request');
                },
                onFailure: () => {
                  hilog.info(0x0000, 'testTag', 'Failed to save request');
                }
              });
              setTimeout(() => {
                this.isClicked = false;
              }, 2000);
            }
          })
      }
      .padding({ left: 16, right: 16 })
      .backgroundColor($r('sys.color.ohos_id_color_list_card_bg'))
      .alignItems(HorizontalAlign.Center)
      .height('100%')
      .width('100%')
// ...
  }
}
```

**说明** 

该示例中，使用了场景化Input作为所在地区的地址选择器，智能填充支持对该地址选择器进行填充。
