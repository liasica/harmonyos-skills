---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/connectivity-kit-faq-0003
title: WiFi信息获取常见问题
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 常见问题 > WiFi信息获取常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:18+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c9e41cc1addcceabbd0274482749a8b75195fe914db42ff45521f429c641b999
---

**Q：设备连接Wi-Fi后，如何获取当前设备的IP地址？**

**A**：使用wifiManager模块获取ipInfo，然后转换为IP常用格式，注意wifiManager.getIpInfo()接口需要权限ohos.permission.GET\_WIFI\_INFO。参考代码如下：

```ts
import { wifiManager } from '@kit.ConnectivityKit';

let ipAddress = wifiManager.getIpInfo().ipAddress;
let ip = (ipAddress >>> 24) + "." + (ipAddress >> 16 & 0xFF) + "." + (ipAddress >> 8 & 0xFF) + "." + (ipAddress & 0xFF);
```

**Q：使用了wifiManager.getLinkedInfo，从WifiLinkedInfo里获取bssid作为WiFi的标识使用，但是从文档上看，只有系统应用才能申请ohos.permission.GET\_WIFI\_LOCAL\_MAC权限获取到真实MAC地址，否则只返回随机地址，有什么方法能获取到WiFi的唯一标识，用于实现WiFi打卡之类的功能？**

**A**：方案设计：

WiFi打卡可通过[geoLocationManager.getCurrentWifiBssidForLocating](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentwifibssidforlocating14)接口，配合[ohos.permission.LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation)和[ohos.permission.APPROXIMATELY\_LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionapproximately_location)权限来获取真实bssid。

* 实现思路：

  权限检查，代码如下：

  ```ts
  /**
     * 判断是否已获取相关权限的授权
     */
    private isPermissionGranted(): boolean {
      try {
        let bundleInfo: bundleManager.BundleInfo =
          bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
        let tokenId: number = bundleInfo.appInfo.accessTokenId;
        return this.atManager.checkAccessTokenSync(tokenId, 'ohos.permission.APPROXIMATELY_LOCATION') ===
        abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED &&
          this.atManager.checkAccessTokenSync(tokenId, 'ohos.permission.LOCATION') ===
        abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
      } catch (error) {
        console.error(`check permission err: ${JSON.stringify(error)}`);
      }
      return false;
    }
  ```

  获取bssid，代码如下：

  ```screen
  /**
     * 获取BSSID
     */
    private getConnectedWiFiBssid() {
      try {
        // 获取连接的Wi-Fi AP（Access Point）的Bssid（Basic Service Set Identifier）信息
        this.bssid = geoLocationManager.getCurrentWifiBssidForLocating();
        console.info(`get wifi bssid:${this.bssid}`);
      } catch (error) {
        console.error(`getCurrentWifiBssidForLocating: errCode:${error.code}, errMessage:${error.message}`);
      }
    }
  ```

* 完整示例代码如下：

  ```screen
  import { geoLocationManager } from '@kit.LocationKit';
  import { abilityAccessCtrl, bundleManager, common } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { JSON } from '@kit.ArkTS';

  @Entry
  @Component
  struct Index {
    @State bssid: string = '';
    private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    private atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

    build() {
      Column({ space: 40 }) {
        Button('点击获取连接WiFi的BSSID')
          .width('60%')
          .onClick(() => {
            if (this.isPermissionGranted()) {
              this.getConnectedWiFiBssid();
            } else {
              this.requestPermissions();
            }
          });

        Text(`BSSID：${this.bssid}`)
          .width('100%')
          .textAlign(TextAlign.Center);

        Button('点击清空数据')
          .width('60%')
          .onClick(() => {
            this.bssid = '';
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }

    /**
     * 判断是否已获取相关权限的授权
     */
    private isPermissionGranted(): boolean {
      try {
        let bundleInfo: bundleManager.BundleInfo =
          bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
        let tokenId: number = bundleInfo.appInfo.accessTokenId;
        return this.atManager.checkAccessTokenSync(tokenId, 'ohos.permission.APPROXIMATELY_LOCATION') ===
        abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED &&
          this.atManager.checkAccessTokenSync(tokenId, 'ohos.permission.LOCATION') ===
        abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
      } catch (error) {
        console.error(`check permission err: ${JSON.stringify(error)}`);
      }
      return false;
    }

    /**
     * 获取BSSID
     */
    private getConnectedWiFiBssid() {
      try {
        // 获取连接的Wi-Fi AP（Access Point）的Bssid（Basic Service Set Identifier）信息
        this.bssid = geoLocationManager.getCurrentWifiBssidForLocating();
        console.info(`get wifi bssid:${this.bssid}`);
      } catch (error) {
        console.error(`getCurrentWifiBssidForLocating: errCode:${error.code}, errMessage:${error.message}`);
      }
    }

    /**
     * 请求权限
     */
    private requestPermissions(): void {
      try {
        this.atManager.requestPermissionsFromUser(this.context, ['ohos.permission.APPROXIMATELY_LOCATION',
          'ohos.permission.LOCATION']).then((data) => {
          // 值0：有权限，则尝试获取BSSID
          if (data.authResults[0] === 0 && data.authResults[1] === 0) {
            this.getConnectedWiFiBssid();
            return;
          }

          // 值非0且非-1：未知值，可能业务逻辑存在问题：如权限名非法等
          if (data.authResults[0] !== -1 && data.authResults[1] !== -1) {
            this.showMyToast(`获取权限失败，检查业务逻辑，错误码：${data.authResults[0]}, ${data.authResults[1]}`);
            return;
          }

          // 值-1：缺少任一权限且已存在弹窗，直接返回，并toast提示
          if (data.dialogShownResults && (data.dialogShownResults[0] || data.dialogShownResults[1])) {
            this.showMyToast(`缺少必要权限，请重试`);
            return;
          }

          // 值-1：缺少任一权限且未弹窗，弹出半模态授权申请
          this.openPermissionsSetting();
        }).catch((err: Error) => {
          console.error(`requestPermissionsFromUser err: ${JSON.stringify(err)}`);
        });
      } catch (err) {
        console.error(`requestPermissionsFromUser err: ${JSON.stringify(err)}`);
      }
    }

    /**
     * 半模态弹窗请求权限
     */
    private openPermissionsSetting(): void {
      this.atManager.requestPermissionOnSetting(this.context, ['ohos.permission.APPROXIMATELY_LOCATION',
        'ohos.permission.LOCATION']).then((grantResult) => {
        if (grantResult[0] === 0 && grantResult[1] === 0) {
          this.getConnectedWiFiBssid();
          return;
        }
        this.showMyToast('缺少必要权限，请重试');
      }).catch((err: BusinessError) => {
        console.error(`data: ${JSON.stringify(err)}`);
      });
    }

    /**
     * 展示toast
     */
    private showMyToast(message: string) {
      try {
        this.getUIContext().getPromptAction().showToast({ duration: 3000, message: message });
      } catch (error) {
        console.error(`show toast occur err: ${JSON.stringify(error)}`);
      }
    }
  }
  ```

**Q：使用[wifiManager.getScanInfoList](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetscaninfolist10)接口扫描出来的bssid与[wifiManager.getLinkedInfo](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfo)接口扫描出的bssid不一致，这是什么原因？**

**A**：wifiManager.getScanInfoList和wifiManager.getLinkedInfo方法分别用于获取WiFi扫描信息列表和已连接的WiFi信息。

如果应用申请了ohos.permission.GET\_WIFI\_LOCAL\_MAC和ohos.permission.GET\_WIFI\_PEERS\_MAC权限（仅系统应用可申请），则返回结果中的bssid为真实设备地址，否则为随机设备地址。两个方法获取的bssid不一致的可能原因如下：

* getScanInfoList和getLinkedInfo方法的调用时间相差较大，由于数据更新和缓存机制导致不一致。
* 多个接入点（AP）使用同一ssid但具有不同的bssid，导致扫描出来的结果不一致。

**Q：wifiManager.getScanInfoList()接口是否有扫描次数限制？**

**A**：wifiManager.getScanInfoList()接口存在扫描频次限制：前台应用2分钟内最多发起4次扫描。参考[扫描管控](../harmonyos-guides/scan-development-guide.md#扫描管控)。

**Q：调用[wifiManager.startScan](../harmonyos-references/js-apis-wifimanager.md#wifimanagerstartscan21)接口频繁发起扫描时返回BusinessError 2501000，是什么原因？**

**A**：wifiManager.startScan接口存在扫描频次限制，应用程序在前台运行时，两分钟内最多可扫描四次。当短时间内频繁调用超过限制时，会返回BusinessError 2501000错误，等待一段时间后再次调用即可正常扫描。错误码详情参考[WIFI错误码](../harmonyos-references/errorcode-wifi.md#section2501000-sta内部异常)。

**Q：同一Wi-Fi断开重连后获取的BSSID不同，是什么原因？如何处理？**

**A**：BSSID是AP（无线接入点）的MAC地址，一个SSID下可以部署多台AP。企业办公网络普遍采用多台AP广播同一SSID的组网方式实现全覆盖和无缝漫游，每台AP有独立的BSSID。手机连接时实际关联的是SSID下的某台AP，断开重连后系统会按信号强度、负载均衡策略重新选择AP，因此获取到的BSSID可能不同。若需在Wi-Fi打卡场景中处理此问题，建议打卡服务端配置同一SSID下全部AP的BSSID白名单，而非预设单一BSSID。应用通过[geoLocationManager.getCurrentWifiBssidForLocating](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentwifibssidforlocating14)获取当前连接Wi-Fi的真实BSSID并上报服务端，服务端判定获取到的BSSID在白名单内即打卡成功。
