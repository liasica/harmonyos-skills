---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-1
title: 安全审计API使用常见问题及解决方案
breadcrumb: FAQ > 系统开发 > 安全 > 设备安全服务（Device Security） > 安全审计API使用常见问题及解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:13+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:bc00bced14fbb87a8917f7adad6d5a34a3c92e309026eaf0935e11b901a3b760
---

## 问题现象

* 问题一：在HarmonyOS应用开发中，使用安全审计权限安装应用时，可能会遇到9568289错误，提示error: install failed due to grant request permissions failed。
* 问题二：在使用Device Security Kit的安全审计能力时，不同的审计事件（例如文件审计和打印审计）复用同一个client进行订阅时是否会产生冲突。
* 问题三：使用安全审计API阻断FILE\_OPEN事件时，设置PROCESS\_NAME\_EQUAL类型的filter进行过滤无效，且调用deny时间歇报错1012000007。
* 问题四：监听安全审计事件0x01C000008（进程创建和退出）时，多个应用启动后获取到的进程UID相同，使用该UID调用[bundleManager.getBundleNameByUidSync](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundlenamebyuidsync14)接口查询对应bundleName时，报错17700021: The specified uid is invalid。
* 问题五：在FILE\_OPEN（0x1C001105）事件处理中打开当前文件会卡顿。
* 问题六：使用安全审计接口订阅应用程序安装拦截事件和应用程序卸载拦截事件时，收到的事件信息内容字段是什么样的？
* 问题七：通过[securityManager.installEnterpriseReSignatureCertificate](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagerinstallenterpriseresignaturecertificate24)安装重签名证书后，未经过重签名的企业应用无法安装，此时重签名校验导致的安装失败，会收到应用程序安装拦截事件吗？
* 问题八：使用安全审计API订阅文件事件时，复制粘贴文件偶发会产生2条file\_write事件。

## 背景知识

* [9568289权限请求失败导致安装失败](../harmonyos-guides/bm-tool.md#section9568289-权限请求失败导致安装失败)：权限请求失败导致安装失败。
* [安全审计](../harmonyos-guides/devicesecurity-audit.md)：提供统一的安全审计数据订阅与取消订阅接口，应用可以获取设备上的安全审计数据，以支撑审计相关业务。
* [ohos.permission.QUERY\_AUDIT\_EVENT](../harmonyos-guides/permissions-for-enterprise-apps.md#ohospermissionquery_audit_event)：允许应用查询安全审计事件。
* [securityAudit.Filter](../harmonyos-references/devicesecurity-securityaudit-api.md#filter)：安全审计过滤器，用于设置事件过滤条件。
* [securityAudit.FilterType](../harmonyos-references/devicesecurity-securityaudit-api.md#filtertype)：安全审计过滤器类型枚举。
* [bundleManager.getBundleNameByUidSync](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundlenamebyuidsync14)：根据UID同步获取对应应用的bundleName。
* [SecurityAudit C API](../harmonyos-references/devicesecurity-capi-securityaudit.md)：安全审计C接口，提供Native层的安全审计客户端创建、事件订阅与过滤能力。
* [securityManager.installEnterpriseReSignatureCertificate](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagerinstallenterpriseresignaturecertificate24)：安装企业重签名证书接口。

## 问题定位

* 场景一：针对问题一，确认当前应用类型为[MDM应用](../harmonyos-guides/mdm-kit.md)还是企业普通应用，非企业应用不可以使用该权限。'ohos.permission.QUERY\_AUDIT\_EVENT'权限在API 12-13时仅面向MDM应用开放；从API 14开始，开放范围变更为企业普通应用。
* 场景一：针对问题一，请确认当前设备类型为2in1设备，当前安全审计[支持的设备](../harmonyos-guides/devicesecurity-introduction.md#支持的设备)仅为PC/2in1。
* 场景二：针对问题二，文件审计和打印审计共用同一个client不会冲突，但安全审计采用统一回调机制下发事件，需要在同一个回调中根据事件ID（eventId）分发到不同的处理逻辑，否则不同审计事件的处理逻辑会混淆。
* 场景三：针对问题三，阻断类事件的监听需要先添加过滤其他事件的filter，再添加需要监听的事件。仅设置目标事件的filter（如PROCESS\_NAME\_EQUAL过滤pid=2）时，filter实际无效，仍会返回所有事件。需要先添加一个排除其他事件的filter，再添加需要监听的事件filter。
* 场景四：针对问题四，安全审计事件0x01C000008上报的进程信息中，procname或cmdline字段即为对应应用的bundleName，该值直接从bundleName获取。审计事件中上报的UID可能并非应用的有效UID，因此通过该UID调用bundleManager.getBundleNameByUidSync接口时会返回17700021错误。
* 场景五：针对问题五，ArkTS层的安全审计客户端性能较差，在处理FILE\_OPEN事件时导致卡顿。在Native层创建客户端可以有效解决该性能问题。
* 场景六：针对问题六，安全审计事件订阅后，回调中返回的事件信息采用统一的结构化格式，包含content、eventId和metadata三个主要字段。content字段包含应用包名、调用方应用包名、调用方uid和事件发生时间戳。metadata字段包含元数据版本、事件日期、设备标识符、关联用户ID和事件分类等信息。
* 场景七：针对问题七，通过securityManager.installEnterpriseReSignatureCertificate安装重签名证书后，未经过重签名的企业应用安装失败属于重签名校验机制的拦截，与安全审计事件订阅的拦截机制不同，不会触发安全审计的应用程序安装拦截事件。
* 场景八：针对问题八，文件操作并非应用直接对文件操作，会使用中间的SA服务进行文件句柄的授权转义，因此一次复制操作出现多次file\_write等文件操作事件是正常现象。

## 分析结论

* 问题一：未申请ohos.permission.QUERY\_AUDIT\_EVENT权限的情况下使用了安全审计能力，或设备与应用类型不符合要求。
* 问题二：复用同一个client订阅不同事件不会产生冲突，但若未在回调中区分事件ID（eventId），则会导致不同审计事件的处理逻辑混淆。
* 问题三：阻断类事件的监听存在隐藏限制，需要先添加过滤其他事件的filter，再添加需要监听的事件。仅设置目标事件的filter无法生效。报错1012000007也与此相关，修复filter后需要重新检查。
* 问题四：安全审计进程创建事件中上报的UID并非应用的有效UID，无法通过bundleManager.getBundleNameByUidSync接口反查bundleName。进程创建事件中的procname或cmdline字段直接包含了bundleName信息，应直接使用该字段获取应用包名。
* 问题五：ArkTS层的安全审计客户端存在语言性能问题，处理FILE\_OPEN事件时出现卡顿。根因为ArkTS的authClient性能较差，在Native层创建客户端可以解决。
* 问题六：安全审计事件信息采用统一的结构化格式，包含事件内容（content）、事件ID（eventId）和事件元数据（metadata）三部分，各字段含义明确。
* 问题七：重签名校验导致的安装失败不会触发安全审计的应用程序安装拦截事件，两者属于不同的拦截机制。
* 问题八：文件操作经过中间SA服务进行文件句柄的授权转义，导致一次复制操作产生多次file\_write事件，属于API特性，非缺陷。

## 修改建议

* 问题一：企业类应用应当先申请ohos.permission.QUERY\_AUDIT\_EVENT权限，然后在PC/2in1设备上使用安全审计能力。
* 问题二：在同一个回调函数中，根据安全审计事件信息中的eventId字段进行条件判断，将不同的事件分发到不同的处理逻辑中。示例代码如下：

  ```ts
  import { securityAudit } from '@kit.DeviceSecurityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  // ...

  let callback = (err: BusinessError, auditEventInfo: securityAudit.AuditEventInfo) => {
    if (err) {
      console.error(`Receive audit event error, code: ${err.code}, message: ${err.message}`);
      return;
    }
    // 根据事件ID分发到不同的处理逻辑
    if (auditEventInfo.eventId === 'FILE_AUDIT_EVENT_ID') {
      // To do handle file audit event.
      console.info('Received file audit event.');
    } else if (auditEventInfo.eventId === 'PRINT_AUDIT_EVENT_ID') {
      // To do handle print audit event.
      console.info('Received print audit event.');
    } else {
      // To do handle other audit events.
      console.info('Received other audit event.');
    }
  };

  try {
    // 复用同一个client传入多个需要订阅的事件ID
    securityAudit.on('auditEvent', ['FILE_AUDIT_EVENT_ID', 'PRINT_AUDIT_EVENT_ID'], callback);
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Subscribe audit event failed, code: ${error.code}, message: ${error.message}`);
  }

  // ...
  ```
* 问题三：在监听阻断类事件前，先添加一个排除其他事件的filter，再添加需要监听的事件。示例代码如下：

  ```ts
  import { securityAudit } from '@kit.DeviceSecurityKit';

  // 先添加过滤其他事件的filter
  let all_filter: securityAudit.Filter = {
    type: securityAudit.FilterType.FILE_PATH_PREFIX,
    isInclude: false,
    values: ['/']
  };
  securityAudit.addFilter(all_filter);

  // 再添加需要监听的事件filter
  let target_filter: securityAudit.Filter = {
    type: securityAudit.FilterType.PROCESS_NAME_EQUAL,
    isInclude: true,
    values: ['2']
  };
  securityAudit.addFilter(target_filter);
  ```

  修复filter后，重新检查deny操作是否仍报错1012000007。
* 问题四：直接使用安全审计事件中上报的procname或cmdline字段作为应用包名，无需通过UID反查bundleName。该字段即为应用的bundleName。
* 问题五：在Native层创建安全审计客户端，使用C API处理FILE\_OPEN事件。示例代码如下：

  ```
  #include "hilog/log.h"
  #undef LOG_DOMAIN
  #undef LOG_TAG
  #define LOG_DOMAIN 0x3200 // Global domain macro
  #define LOG_TAG "MY_TAG"  // Global tag macro
  #include "DeviceSecurityKit/security_audit.h"

  SecurityAudit_AuthClient* client = nullptr;

  void sec_handler(const SecurityAudit_Event *events, uint64_t count) {
      if (events == nullptr) {
          return;
      }
      OH_LOG_INFO(LOG_APP, "sec_handler %{public}lu %{private}s", count, events->content);
      if (count > 0) {
          // 默认放通，如需审计敏感信息并决定是否阻断，建议另起线程处理
          HMS_SecurityAudit_Auth(client, events, SECURITY_AUDIT_AUTH_RESULT_ALLOW);
      }
      return;
  }

  void NewAuthClient(napi_env env, napi_callback_info info) {
      if (canIUse("SystemCapability.Security.SecurityAudit")) {
          // 释放已有client，避免句柄泄漏
          if (client != nullptr) {
              HMS_SecurityAudit_DestroyAuthClient(client);
              client = nullptr;
          }

          int32_t res = HMS_SecurityAudit_NewAuthClient(&client, sec_handler);
          if (res != 0) {
              OH_LOG_INFO(LOG_APP, "NewAuthClient failed! res %d", res);
              return;
          }

          SecurityAudit_Filter excludeFilter;
          const char* excludeRootPath = {"/"};
          excludeFilter.isInclude = false;
          excludeFilter.type = SECURITY_AUDIT_FILTER_TYPE_FILE_PATH_PREFIX;
          excludeFilter.value = &excludeRootPath;
          excludeFilter.valueCount = 1;

          SecurityAudit_Filter includeFilter;
          const char* includeAppSandboxPath = {"/data/app/el2/100/base/com.example.myapplication"};
          includeFilter.isInclude = true;
          includeFilter.type = SECURITY_AUDIT_FILTER_TYPE_FILE_PATH_PREFIX;
          includeFilter.value = &includeAppSandboxPath;
          includeFilter.valueCount = 1;

          res = HMS_SecurityAudit_AddAuthEventFilter(client, SECURITY_AUDIT_AUTH_EVENT_FILE_OPEN, &excludeFilter);
          if (res != 0) {
              OH_LOG_INFO(LOG_APP, "AddAuthEventFilter excludeFilter failed! res %d", res);
              return;
          }

          res = HMS_SecurityAudit_AddAuthEventFilter(client, SECURITY_AUDIT_AUTH_EVENT_FILE_OPEN, &includeFilter);
          if (res != 0) {
              OH_LOG_INFO(LOG_APP, "AddAuthEventFilter includeFilter failed! res %d", res);
              return;
          }

          const SecurityAudit_Auth_Event event = {SECURITY_AUDIT_AUTH_EVENT_FILE_OPEN};
          res = HMS_SecurityAudit_SubscribeAuthEvent(client, &event, 1);
          if (res != 0) {
              OH_LOG_INFO(LOG_APP, "SubscribeAuthEvent failed! res %d", res);
          }
      }
  }
  ```

  **说明** 

  回调中默认调用ALLOW放通当前事件。如需审计文件敏感信息并决定是否阻断，建议另起一个线程处理，处理完毕后再调用HMS\_SecurityAudit\_Auth接口给出ALLOW或DENY结果，避免阻塞，提高性能。
* 问题六：安全审计事件信息内容字段结构如下：

  ```json
  {
    "content": {
      "bundleName": "%s", // 应用包名
      "callingBundleName": "%s", // 调用方应用包名
      "callingUid": %d, // 调用方uid
      "timestamp_utc": %d // 事件发生时间戳
    },
    "eventId": %d, // 事件id
    "metadata": {
      "version": "%s", // 元数据版本（空值未指定）
      "date": "%s", // 事件日期（空值未指定）
      "deviceId": "%s", // 设备标识符（空值未指定）
      "userId": %d, // 关联用户ID（1为系统默认）
      "eventType": %d // 本事件分类（1代表阻断类事件，0代表通知类事件）
    }
  }
  ```
* 问题七：不会触发应用程序安装拦截事件。重签名校验失败属于证书校验层面的拦截，与安全审计事件订阅无关。
* 问题八：可以根据file\_size区分两条file\_write事件，测试表明会产生一个size=0和size正常的事件。但需注意存在size天生为0的文件（如空的txt文件），且低版本可能只会有1条事件。
