---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-workspace-authentication
title: 企业账号认证
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 企业账号认证
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99699ebefdf80aa04b61bc6766ec848692c2eab762f81c09ef988ac3fdaa00bf
---

从API版本6.1.0(23)开始，支持企业认证和获取企业应用令牌的能力。

## 场景介绍

Enterprise Space Kit为企业应用提供企业账号认证的能力。在企业空间初始化阶段，实现企业用户的账号认证。同时支持获取企业应用令牌的能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#authenticate)。

| 接口名 | 描述 |
| --- | --- |
| [authenticate](../harmonyos-references/enterprisespace-spacemanager.md#authenticate)(enterpriseAuthInfo: [WorkspaceDomainInfo](../harmonyos-references/enterprisespace-spacemanager.md#workspacedomaininfo), credential: Uint8Array): Promise<[AuthResult](../harmonyos-references/enterprisespace-spacemanager.md#authresult)> | 企业账号认证并返回结果。 |
| [getAccessToken](../harmonyos-references/enterprisespace-spacemanager.md#getaccesstoken)(businessParams: Record<string, string>): Promise<Uint8Array> | 获取企业应用令牌并返回结果。 |

## 开发步骤

1.导入企业账号认证API模块相关依赖。

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

2.企业账号认证API接口封装。

```typescript
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class WorkspaceCertificationApi {
  static async authenticate(enterpriseAuthInfo: spaceManager.WorkspaceDomainInfo,
    credential: Uint8Array): Promise<spaceManager.AuthResult | undefined> {
    try {
      const authResult: spaceManager.AuthResult = await spaceManager.authenticate(enterpriseAuthInfo, credential);
      hilog.info(DOMAIN, TAG, `Succeeded in authenticating. Auth result is: ` + JSON.stringify(authResult));
      return authResult;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to authenticate. Code: ${err.code}, message: ${err.message}`);
      return undefined;
    }
  }

  static async getAccessToken(params: Record<string, string>): Promise<Uint8Array | undefined> {
    try {
      const result: Uint8Array = await spaceManager.getAccessToken(params);
      hilog.info(DOMAIN, TAG, `Succeeded in getting access token. Result is: ` + JSON.stringify(result));
      return result;
    } catch (err) {
      hilog.error(DOMAIN, TAG,`Failed to get access token. Code: ${err.code}, message: ${err.message}`);
      return undefined;
    }
  }
}
```

3.导入企业账号认证业务实现相关依赖。

```typescript
import { router } from '@kit.ArkUI';
import { osAccount } from '@kit.BasicServicesKit';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { WorkspaceCertificationApi } from '../api/WorkspaceCertificationApi'
```

4.企业账号认证业务相关实现。

```typescript
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

enum AuthModeType {
  SASL = 'SASL',
}

enum CertifiedProtocolType {
  GSSAPI = 'GSSAPI/Kerberos',
  OAUTH2 = 'OAuth 2.0',
}

enum LdapEncryptMode {
  LDAP = 'LDAP',
  LDAPS = 'LDAPS',
  LDAP_STARTTLS = 'LDAP STARTTLS',
}

enum ServerType {
  NONE = '',
  LDAP = 'LDAP',
  AD = 'AD',
  IDaaS = 'IDaaS',
}

type ADConfig = Record<string, string>;
type LDAPConfig = Record<string, string>;
type OAuthConfig = Record<string, string>;
type IDaaSConfig = Record<string, string | OAuthConfig>;
type ServerConfigParams = Record<string, string | ADConfig | LDAPConfig | IDaaSConfig>;
type ServerConfig = Record<string, string | ServerConfigParams>;

@Entry
@Component
struct WorkspaceCertificationPage {
  /**
   * 获取IDaaS协议服务器配置
   * @returns
   */
  public getIDaaSServerConfig(): ServerConfig {
    const idaasConfigData: IDaaSConfig = {
      'authProtocol': 'OAuth 2.0',
      'oauthConfig': {
        'userAuthenRequestUri': 'iDaaSUserAuthUrl',
        'authorizationRequestUri': 'iDaaSAuthUrl',
        'tokenRequestUri': 'iDaaSTokenUrl',
        'userInfoRequestUri': 'iDaaSUserUrl',
        'clientId': 'iDaaSClientID',
        'clientSecret': 'iDaaSClientSecret',
        'scope': 'iDaaSScope',
        'accountIdAttributeName': 'iDaaSAccountID',
        'accountNameAttributeName': 'iDaaSAccountName',
      },
    };
    const parameters: ServerConfigParams = {
      'serverType': ServerType.IDaaS,
      'idaasConfig': idaasConfigData,
    };
    const serverConfig: ServerConfig = {
      'parameters': parameters,
    };
    return serverConfig;
  }

  /**
   * 获取LDAP协议服务器配置
   * @returns
   */
  private getLDAPServerConfig(): ServerConfig {
    const ldapConfig: LDAPConfig = {
      'authServerAddress': 'domainName',
      'authenMode': AuthModeType.SASL,
      'authenProtocol': CertifiedProtocolType.GSSAPI,
      'kdcAddress': 'kdcAddress',
      'accountIdAttributeName': 'accountId',
      'accountNameAttributeName': 'accountName',
      'encryptMode': LdapEncryptMode.LDAP,
      'ldapPort': 'portNum',
      'baseDN': 'baseDN',
    };
    if (ldapConfig['encryptMode'] !== LdapEncryptMode.LDAP) {
      ldapConfig['kdcAddress'] = '';
    }
    const parameters: ServerConfigParams = {
      'ldapConfig': ldapConfig,
    };
    const serverConfig: ServerConfig = {
      'authServerName': ldapConfig['authServerAddress'],
      'parameters': parameters,
    };
    return serverConfig;
  }

  /**
   * 获取AD协议服务器配置
   * @returns
   */
  private getADServerConfig(): ServerConfig {
    const adConfig: ADConfig = {
      'adDomain': 'domainName',
      'authenMode': AuthModeType.SASL,
    };
    const parameters: ServerConfigParams = {
      'adConfig': adConfig,
    };
    const serverConfig: ServerConfig = {
      'authServerName': 'domainName',
      'parameters': parameters,
    };
    return serverConfig;
  }

  private getServiceConfig(serverType: string): ServerConfig {
    let serverConfig: ServerConfig;
    if (serverType === ServerType.IDaaS) {
      serverConfig = this.getIDaaSServerConfig();
    } else if (serverType === ServerType.LDAP) {
      serverConfig = this.getLDAPServerConfig();
    } else {
      serverConfig = this.getADServerConfig();
    }

    return serverConfig;
  }

  async authenticate() {
    let serverType = ServerType.AD;
    let serverConfig: ServerConfig = this.getServiceConfig(serverType); // 由用户设置对应域服务器的配置参数
    let serverConfigId: string = 'serverConfigId';

    try {
      // 绑定域服务器
      await osAccount.DomainServerConfigManager.addServerConfig(serverConfig);
      // 获取域服务器ID
      let servers: osAccount.DomainServerConfig[] = await osAccount.DomainServerConfigManager.getAllServerConfigs();
      servers.forEach((server) => {

        // 过滤非目标服务器

        serverConfigId = server.id;
      });
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to config domain server. Code: ${err.code}, message: ${err.message}`);
    }

    const enterpriseAuthInfo: spaceManager.WorkspaceDomainInfo = {
      domain: 'testDomain', // 域名
      workspaceName: 'testAccountName', // 工作空间域账号名称
      serverConfigId: serverConfigId // 工作空间所属域的服务器配置标识符，绑定域服务器后本地生成
    };
    const credential = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 0]); // 示例：员工密码的ASCII码
    const authResult: spaceManager.AuthResult | undefined =
      await WorkspaceCertificationApi.authenticate(enterpriseAuthInfo, credential);
    if (authResult === undefined) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to authenticate!');
      return;
    }
    // 处理后置逻辑
  }

  async getAccessToken() {
    const params: Record<string, string> = {
      'clientId': 'test1' // 业务参数，由业务方根据请求协议自定义，企业应用在域服务器的唯一标识
    };

    const result: Uint8Array | undefined =
      await WorkspaceCertificationApi.getAccessToken(params); // 从域服务器获取的一次性授权码，可使用授权码与域服务器直接交互。
    if (result === undefined) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to get access token!');
      return;
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.authenticate'))
          .buttonCommonStyle()
          .onClick(() => {
            this.authenticate();
          })
      }

      Row() {
        Button($r('app.string.getAccessToken'))
          .buttonCommonStyle()
          .onClick(() => {
            this.getAccessToken();
          })
      }

      Row() {
        Button($r('app.string.back'))
          .buttonCommonStyle()
          .onClick(() => {
            router.back();
          })
      }
    }
  }
}

@Extend(Button)
function buttonCommonStyle() {
  .width(200)
  .height(50)
  .backgroundColor('#6366F1')
  .fontColor('#FFFFFF')
  .fontSize(14)
  .margin({ left: 20, bottom: 5 })
}
```
