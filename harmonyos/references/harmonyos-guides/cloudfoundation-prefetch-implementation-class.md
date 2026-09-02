---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-implementation-class
title: 预加载实现类
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 添加预加载依赖类 > 预加载实现类
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:053de52955f1efce109eace4b4b2175df27477e9eaeb1f33f734ea0db96319f0
---

在“entry/src/main/ets/prefetchUtil”目录下新增PrefetchUtil.ets和PrefetchWrapper.ets。

PrefetchUtil和PrefetchWrapper实现类功能如下：

* PrefetchUtil：预加载API的封装类，为PrefetchWrapper提供预加载API封装接口。

  + 提供安装预加载的数据获取接口
  + 提供周期性预加载的任务注册接口和数据获取接口
  + 提供周期性预加载是否已拉取数据的判断接口
* PrefetchWrapper：预加载包装类，为页面提供预加载封装接口。

  + 提供安装预加载数据获取和渲染接口
  + 提供周期性预加载数据获取和渲染接口
  + 提供安装预加载和周期性预加载数据获取和渲染接口

## PrefetchUtil

周期性预加载任务注册间隔需要大于12h，建议按照如下示例取值为24h。

```typescript
import { cloudResPrefetch } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { PreferenceUtil } from '../common/PreferenceUtil';
import { GlobalContext } from '../common/GlobalContext';

const PREFERENCES_PREFETCH_STORE_NAME = 'defaultStore';
const PREFERENCES_PREFETCH_FIRST_REGISTER_TIME = 'prefetchTaskFirstRegisterTime'; // 首次注册时间
const PREFERENCES_PREFETCH_TASK_EXPIRE_TIME = 'prefetchTaskExpireTime'; // 任务过期时间
const PREFETCH_TASK_REGISTER_INTERVAL = 24 * 60 * 60 * 1000; // 24h < 72h
const PREFETCH_DATA_UPDATE_INTERVAL = 12 * 60 * 60 * 1000; // 12h
const HILOG_DOMAIN = 0x0000;
const TAG = 'Prefetch';

export class PrefetchUtil {
  private static timeoutId: number = (0 - Number.MAX_VALUE);
  private static hasPrefetchedData: boolean = false;
  private static isPrefetchTaskRegistered: boolean = false;
  private static now: number = (0 - Number.MAX_VALUE);

  private constructor() {
  }

  /**
   * 预加载数据获取
   * @param type 安装预加载/周期预加载数据
   * @throws 预加载getPrefetchResult API异常
   * @returns PrefetchResult
   */
  public static async getPrefetchResult(type: cloudResPrefetch.PrefetchMode) {
    return cloudResPrefetch.getPrefetchResult(type);
  }

  /**
   * 周期性预加载应用注册任务，间隔24h
   * @param token 应用/用户级token，可以为空
   * @param params 自定义筛选参数，定义为JSON格式，可以为空
   * @param forceRegister 是否强制注册
   */
  public static async registerPrefetchTask(token: string, params: string | object,
    forceRegister: boolean = false) {
    await PrefetchUtil.updatePrefetchTaskInfo();
    if (!forceRegister) {
      await PrefetchUtil.registerPrefetchTaskNotForced(token, params);
      return;
    }
    await PrefetchUtil.registerPrefetchTaskForced(token, params);
  }

  /**
   * 是否有周期性预加载数据：如果是首次注册，12h后才有周期性预加载数据
   * @returns boolean
   */
  public static hasPrefetchTaskData(): boolean {
    return PrefetchUtil.hasPrefetchedData;
  }

  private static async updatePrefetchTaskInfo() {
    PrefetchUtil.now = Date.now();
    if (PrefetchUtil.timeoutId != 0 - Number.MAX_VALUE) {
      clearTimeout(PrefetchUtil.timeoutId);
    }
    let firstRegisterTime = await PreferenceUtil.getValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME,
      PREFERENCES_PREFETCH_FIRST_REGISTER_TIME) as number;
    if (firstRegisterTime) {
      PrefetchUtil.isPrefetchTaskRegistered = true;
      // 判断任务是否已获取数据(首次注册后12h，之后数据每隔12h更新一次)
      if (PrefetchUtil.now - firstRegisterTime >= PREFETCH_DATA_UPDATE_INTERVAL) {
        PrefetchUtil.hasPrefetchedData = true;
      }
    }
    if (!PrefetchUtil.isPrefetchTaskRegistered) {
      hilog.info(HILOG_DOMAIN, TAG, `first register time: ${PrefetchUtil.now}`);
      await PreferenceUtil.setValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME,
        PREFERENCES_PREFETCH_FIRST_REGISTER_TIME, PrefetchUtil.now);
    }
  }

  private static async registerPrefetchTaskForced(token: string, params: string | object) {
    // 过期或强制更新任务注册
    let expireTime = PrefetchUtil.now + PREFETCH_TASK_REGISTER_INTERVAL;
    hilog.info(HILOG_DOMAIN, TAG, `new expireTime: ${expireTime}`);
    await PreferenceUtil.setValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME,
      PREFERENCES_PREFETCH_TASK_EXPIRE_TIME, expireTime);
    // 更新任务注册和定时器
    PrefetchUtil.registerPrefetchTaskWithApi(token, params);
    PrefetchUtil.updateTaskTimer(PREFETCH_TASK_REGISTER_INTERVAL);
  }

  private static async registerPrefetchTaskNotForced(token: string, params: string | object) {
    // 判断任务到期，重新注册
    let expireTime = await PreferenceUtil.getValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME,
      PREFERENCES_PREFETCH_TASK_EXPIRE_TIME) as number;
    if (expireTime && (PrefetchUtil.now < expireTime)) {
      // 任务没有过期：只更新定时器
      let delay = expireTime - PrefetchUtil.now;
      hilog.info(HILOG_DOMAIN, TAG, `not expire, delay:${delay}`);
      PrefetchUtil.updateTaskTimer(delay);
      return;
    }
    await PrefetchUtil.registerPrefetchTaskForced(token, params);
  }

  private static registerPrefetchTaskWithApi(token: string, params: string | object) {
    try {
      cloudResPrefetch.registerPrefetchTask({
        token: token,
        params: params
      });
      hilog.info(HILOG_DOMAIN, TAG, `register success`);
    } catch (error) {
      hilog.error(HILOG_DOMAIN, TAG, `register catch = ${error.message}`);
    }
  }

  private static updateTaskTimer(delay: number) {
    PrefetchUtil.timeoutId = setTimeout(() => {
      if (PrefetchUtil.timeoutId != (0 - Number.MAX_VALUE)) {
        clearInterval(PrefetchUtil.timeoutId);
        PrefetchUtil.timeoutId = (0 - Number.MAX_VALUE);
      }
    }, delay);
  }
}
```

## PrefetchWrapper

* 预加载数据获取成功时，需要增加页面的渲染逻辑。
* 预加载数据获取失败时，需要做数据降级处理。如下示例代码以cloudFunctionCall接口触发云函数为例获取数据，请根据实际业务实现进行修改。

  需要注意以下两点：

  1. 使用cloudFunctionCall接口之前，请先[设置云函数配置项](cloudfoundation-call-function.md#设置云函数配置项)。
  2. 测试周期性预加载时，需要将下文示例代码periodicPrefetch方法中的如下代码块注释。若不注释，则需等待12h才能获取周期性预加载数据。

     ```typescript
     if (!PrefetchUtil.hasPrefetchTaskData()) { // 是否有周期性预加载数据：如果是首次注册，12h后才有周期性预加载数据
       hilog.info(HILOG_DOMAIN, TAG, 'not has prefetch data');
       this.cloudFunctionCall(); // 使用普通方式获取应用数据
       return;
     }
     ```

     测试完成后，取消上述代码块注释即可。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cloudFunction, cloudResPrefetch } from '@kit.CloudFoundationKit';
import { PrefetchUtil } from './PrefetchUtil';
import { PreferenceUtil } from '../common/PreferenceUtil';
import { BusinessError } from '@kit.BasicServicesKit';
import { GlobalContext } from '../common/GlobalContext';
import { deferredLink } from '@kit.AppLinkingKit';

const HILOG_DOMAIN = 0x0000;
const TAG = 'PrefetchWrapper';
const PREFETCH_MODE = 'prefetchMode';
const PREFETCH_LINK_MODE = 'prefetchLinkMode';
const PREFERENCES_PREFETCH_STORE_NAME = 'defaultStore';

export class PrefetchWrapper {
  private static instance: PrefetchWrapper;
  private prefetchMode: number = 0;
  private linkPrefetchMode: number = 0;

  private constructor() {
  }

  public static getInstance(): PrefetchWrapper {
    if (!PrefetchWrapper.instance) {
      PrefetchWrapper.instance = new PrefetchWrapper();
    }
    return PrefetchWrapper.instance;
  }

  // 支持所有预加载类型
  public async doPrefetch() {
    // 应用安装后首次打开：优先使用跳链安装预加载
    await this.doLinkPrefetch();
    // 初始化prefetchMode
    this.initPrefetchMode();
    if (!this.prefetchMode) {
      // 应用安装后首次打开：使用安装预加载
      hilog.info(HILOG_DOMAIN, TAG, `installPrefetch`);
      this.installPrefetch();
      this.setPrefetchMode(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH);
    } else {
      // 应用安装后非首次打开：使用周期性预加载
      hilog.info(HILOG_DOMAIN, TAG, `periodicPrefetch: ${this.prefetchMode}`);
      this.periodicPrefetch();
    }
  }

  // 仅支持安装预加载
  public doInstallPrefetch() {
    // 初始化prefetchMode
    this.initPrefetchMode();
    if (!this.prefetchMode) {
      // 应用安装后首次打开：使用安装预加载
      hilog.info(HILOG_DOMAIN, TAG, `installPrefetch`);
      this.installPrefetch();
      this.setPrefetchMode(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH);
    }
  }

  // 仅支持周期性预加载
  public doPeriodicPrefetch() {
    // 初始化prefetchMode
    this.initPrefetchMode();
    if (!this.prefetchMode) {
      this.setPrefetchMode(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH);
    } else {
      // 应用安装后非首次打开：使用周期性预加载
      hilog.info(HILOG_DOMAIN, TAG, `periodicPrefetch: ${this.prefetchMode}`);
      this.periodicPrefetch();
    }
  }

  // 支持跳链安装预加载：应用安装后10分钟内有效
  public async doLinkPrefetch(): Promise<boolean> {
    try {
      let link = await this.popPrefetchLink();
      if (link.length < 1) {
        hilog.error(HILOG_DOMAIN, TAG, `get install link null`);
        return Promise.resolve(false);
      }
      let params: cloudResPrefetch.PrefetchParams = {
        link: link
      };
      let dataResult = await cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.LINK_PREFETCH, params);
      // todo 处理dataResult，跳转应用详情页并渲染
      hilog.info(HILOG_DOMAIN, TAG, `get install link prefetch dataResult: ${JSON.stringify(dataResult)}`);
      return Promise.resolve(true);
    } catch (err) {
      return Promise.resolve(false);
    }
  }

  private installPrefetch() {
    PrefetchUtil.getPrefetchResult(cloudResPrefetch.PrefetchMode.INSTALL_PREFETCH)
      .then((data: cloudResPrefetch.PrefetchResult) => { // 接口调用成功，处理缓存的应用数据
        hilog.info(HILOG_DOMAIN, TAG, `get install prefetch cache successfully`);
        let dataResult = data.result; // data.result即是缓存的应用数据
        // todo 处理dataResult
        hilog.info(HILOG_DOMAIN, TAG, `get install prefetch dataResult: ${JSON.stringify(dataResult)}`);
      })
      .catch((err: BusinessError) => {
        hilog.error(HILOG_DOMAIN, TAG, `get install prefetch cache failed: ${err.message}, ${err.code}`);
        this.cloudFunctionCall(); // 应用走原有逻辑获取数据，示例使用云函数获取
      });
  }

  private initPrefetchMode() {
    if (!this.prefetchMode) {
      let context = GlobalContext.getContext();
      this.prefetchMode =
        PreferenceUtil.getValueSync(context, PREFERENCES_PREFETCH_STORE_NAME, PREFETCH_MODE) as number;
    }
  }

  private setPrefetchMode(mode: number) {
    PreferenceUtil.setValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME, PREFETCH_MODE, mode);
  }

  private initLinkPrefetchMode() {
    if (!this.linkPrefetchMode) {
      let context = GlobalContext.getContext();
      this.linkPrefetchMode =
        PreferenceUtil.getValueSync(context, PREFERENCES_PREFETCH_STORE_NAME, PREFETCH_LINK_MODE) as number;
    }
  }

  private setLinkPrefetchMode(mode: number) {
    PreferenceUtil.setValue(GlobalContext.getContext(), PREFERENCES_PREFETCH_STORE_NAME, PREFETCH_LINK_MODE, mode);
  }

  private initPeriodPrefetch() {
    let token = ''; // 应用自定义token参数，通常作为鉴权参数使用。在开发云侧云函数时，可以提取鉴权信息，也可以不进行鉴权。如果不需要鉴权，该参数可以为空
    let params = ''; // 应用自定义params参数，通常作为筛选参数使用，可以定义为JSON格式。在开发云侧云函数时，可以提取该参数进行筛选。如果不需要筛选，该参数可以为空
    PrefetchUtil.registerPrefetchTask(token, params);
  }

  private periodicPrefetch() {
    this.initPeriodPrefetch();
    if (!PrefetchUtil.hasPrefetchTaskData()) { // 是否有周期性预加载数据：如果是首次注册，12h后才有周期性预加载数据
      hilog.info(HILOG_DOMAIN, TAG, `not has prefetch data`);
      this.cloudFunctionCall(); // 使用普通方式获取应用数据
      return;
    }
    PrefetchUtil.getPrefetchResult(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH)
      .then((data: cloudResPrefetch.PrefetchResult) => { // 接口调用成功，处理缓存的应用数据
        hilog.info(HILOG_DOMAIN, TAG, `get periodic prefetch cache successfully`);
        let dataResult = data.result; // data.result即是缓存的应用数据
        let timestamp = data.timestamp; // data.timestamp即是缓存拉取时间
        let token = data.token; // data.token即是注册任务token
        // todo 处理dataResult
        hilog.info(HILOG_DOMAIN, TAG, `get periodic prefetch dataResult: ${JSON.stringify(dataResult)}`);
        hilog.info(HILOG_DOMAIN, TAG, `get periodic prefetch timestamp: ${timestamp.toString()}`);
        hilog.info(HILOG_DOMAIN, TAG, `get periodic prefetch token: ${token}`);
      })
      .catch((err: BusinessError) => {
        hilog.error(HILOG_DOMAIN, TAG, `get periodic prefetch cache failed: ${err.message}, ${err.code}`);
        this.cloudFunctionCall(); // 应用走原有逻辑获取数据，示例使用云函数获取
      });
  }

  // 获取跳链安装预加载的链接信息
  private async popPrefetchLink(): Promise<string> {
    this.initLinkPrefetchMode();
    if (this.linkPrefetchMode) {
      return Promise.resolve('');
    }
    this.setLinkPrefetchMode(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH);
    try {
      let link = await deferredLink.popDeferredLink();
      return Promise.resolve(link);
    } catch (err) {
      return Promise.resolve('');
    }
  }

  private cloudFunctionCall() {
    hilog.info(HILOG_DOMAIN, TAG, `cloudFunctionCall start`);
    cloudFunction.call({
      name: 'function_name', // 需修改为实际的云函数名称
      timeout: 5 * 1000
    }).then((data: cloudFunction.FunctionResult) => {
      hilog.info(HILOG_DOMAIN, TAG, `call function successfully`);
      let dataResult = data.result; // data.result即是缓存的应用数据
      // todo 处理dataResult
      hilog.info(HILOG_DOMAIN, TAG, `call function get: ${JSON.stringify(dataResult)}`);
    }).catch((err: BusinessError) => {
      hilog.error(HILOG_DOMAIN, TAG, `call function failed: ${err.message}`);
    });
  }
}
```
