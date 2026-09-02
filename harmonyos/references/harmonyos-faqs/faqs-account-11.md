---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-11
title: LoginWithHuaweiIDButton能否根据loginType的属性动态切换登录类型
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > LoginWithHuaweiIDButton能否根据loginType的属性动态切换登录类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:dca01531d6135b7b3f2090df7ea516ca5dd0bd894147d7bf026df2bc486a8c51
---

## 问题现象

使用LoginWithHuaweiIDButton一键登录组件，希望根据组件的loginType属性动态改变组件类型，比如获取到匿名手机号就使用一键登录，不存在就使用华为账号登录，实际使用时为什么状态更新后，UI组件没有变化？

问题代码如下：

```ts
// 华为一键登录按钮组件
LoginWithHuaweiIDButton({
  params: {
    textAndIconStyle: true,
    style: loginComponentManager.Style.BUTTON_BLACK,
    extraStyle: {
      buttonStyle: new loginComponentManager.ButtonStyle()
    },
    // 存在匿名手机号则使用手机号一键登录，不存在则使用华为账号登录
    loginType: this.loginType,
  },
  controller: this.controller,
})
@Computed
  get loginType() {
    return this.quickLoginAnonymousPhone ? loginComponentManager.LoginType.QUICK_LOGIN :
    loginComponentManager.LoginType.ID
  }
```

## 背景知识

* [LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md)：华为账号登录组件，通过该组件，应用可完成华为账号的登录功能。
* [loginType](../harmonyos-references/account-api-component-manager.md#logintype)：是LoginWithHuaweiIDButton中标识华为账号登录类型的属性，默认是LoginType.ID，一键登录对应的值是LoginType.QUICK\_LOGIN。
* 华为账号一键登录及华为账号登录，可以[借助DevEco Studio辅助开发](../harmonyos-guides/account-phone-unionid-login.md#借助deveco-studio辅助开发可选)，快速实现页面代码及逻辑编写。

## 解决方案

因LoginWithHuaweiIDButton中封装了登录相关的业务逻辑，不支持根据loginType动态改变登录类型，上述需求可通过if/else控制实际显示的登录组件来实现。

核心代码如下：

```ts
aboutToAppear(): void {
  // 页面初始化时，获取匿名手机号
  this.getQuickLoginAnonymousPhone();
}

build() {
  Column() {
    // 获取到匿名手机号，走一键登录
    if (this.quickLoginAnonymousPhone) {
      QuickLoginButtonComponent({ quickLoginAnonymousPhone: this.quickLoginAnonymousPhone });
    } else {
      // 未获取匿名手机号，走华为账号登录
      LoginButtonComponent();
    }
  }
  .height('100%')
  .width('100%');
}
```

完整示例代码：

```ts
import { authentication, loginComponentManager, LoginWithHuaweiIDButton } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

const LOG_TAG: string = 'QuickLoginButtonComponent';
const DOMAIN_ID: number = 0x0000;

@Entry
@Component
struct Index {
  @State quickLoginAnonymousPhone: string = '';

  getQuickLoginAnonymousPhone() {
    // 创建授权请求，并设置参数
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    // 获取匿名手机号需传quickLoginAnonymousPhone这个scope，传参之前需要先申请“华为账号一键登录”权限
    //(权限名称为：quickLoginMobilePhone),后续才能获取匿名手机号数据
    authRequest.scopes = ['quickLoginAnonymousPhone'];
    // 用于防跨站点请求伪造
    authRequest.state = util.generateRandomUUID();
    // 一键登录场景该参数只能设置为false
    authRequest.forceAuthorization = false;
    const controller = new authentication.AuthenticationController();
    try {
      controller.executeRequest(authRequest).then((response: authentication.AuthorizationWithHuaweiIDResponse) => {
        // 获取到UnionID、OpenID、匿名手机号
        const unionID = response.data?.unionID;
        const openID = response.data?.openID;
        const anonymousPhone = response.data?.extraInfo?.quickLoginAnonymousPhone as string;
        if (anonymousPhone) {
          hilog.info(DOMAIN_ID, LOG_TAG, 'Succeeded in authentication.');
          this.quickLoginAnonymousPhone = anonymousPhone;
          return;
        }
        hilog.info(DOMAIN_ID, LOG_TAG, 'Succeeded in authentication. AnonymousPhone is empty.');
        // 未获取到匿名手机号需要跳转到应用自定义的登录页面
      }).catch((error: BusinessError) => {
        hilog.error(DOMAIN_ID, LOG_TAG,
          `Failed to login, errorCode is ${error.code}, errorMessage is ${error.message}`);
      });
    } catch (error) {
      hilog.error(DOMAIN_ID, LOG_TAG,
        `Failed to login, errorCode is ${error.code}, errorMessage is ${error.message}`);
    }
  }

  aboutToAppear(): void {
    // 页面初始化时，获取匿名手机号
    this.getQuickLoginAnonymousPhone();
  }

  build() {
    Column() {
      // 获取到匿名手机号，走一键登录
      if (this.quickLoginAnonymousPhone) {
        QuickLoginButtonComponent({ quickLoginAnonymousPhone: this.quickLoginAnonymousPhone });
      } else {
        // 未获取匿名手机号，走华为账号登录
        LoginButtonComponent();
      }
    }
    .height('100%')
    .width('100%');
  }
}

@Component
struct LoginButtonComponent {
  logTag: string = 'LoginButtonComponent';
  domainId: number = 0x0000;
  /**
   * Defines the controller to interact with the button for login with a HUAWEI ID.
   */
  controller: loginComponentManager.LoginWithHuaweiIDButtonController =
    new loginComponentManager.LoginWithHuaweiIDButtonController()
      .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
        if (error) {
          hilog.error(this.domainId, this.logTag,
            `Failed to login with LoginWithHuaweiIDButton. Code is ${error.code}, message is ${error.message}`);
          return;
        }

        if (response) {
          hilog.info(this.domainId, this.logTag, 'Succeed in clicking LoginWithHuaweiIDButton.');
          let authCode = response.authorizationCode;
          let openID = response.openID;
          let unionID = response.unionID;
          let idToken = response.idToken;
          // to do something after getting the response.
          return;
        }
      });

  build() {
    Column() {
      Column() {
        /**
         * Invoke the LoginWithHuaweiIDButton component.
         */
        LoginWithHuaweiIDButton({
          params: {
            style: loginComponentManager.Style.BUTTON_RED,
            loginType: loginComponentManager.LoginType.ID,
            supportDarkMode: true,
          },
          controller: this.controller
        });
      }
      .height(40)
      .width(200)
      .margin({
        left: $r('sys.float.ohos_id_max_padding_start'),
        right: $r('sys.float.ohos_id_max_padding_end')
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}

@Component
struct QuickLoginButtonComponent {
  // 匿名化手机号
  @Prop quickLoginAnonymousPhone: string;
  // 是否勾选协议
  @State isSelected: boolean = false;
  // 华为账号用户认证协议链接，此处仅为示例，实际开发过程中，出于可维护性、安全性等方面考虑，域名不建议硬编码在本地
  private static USER_AUTHENTICATION_PROTOCOL: string =
    'https://*********/legal/id/authentication-terms.htm?code=CN&language=zh-CN';
  private static USER_SERVICE_TAG = '用户服务协议';
  private static PRIVACY_TAG = '隐私协议';
  private static USER_AUTHENTICATION_TAG = '华为账号用户认证协议';
  // 定义LoginWithHuaweiIDButton展示的隐私文本，展示应用的用户服务协议、隐私协议和华为账号用户认证协议
  privacyText: loginComponentManager.PrivacyText[] = [{
    text: '已阅读并同意',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }, {
    text: '《用户服务协议》',
    tag: QuickLoginButtonComponent.USER_SERVICE_TAG,
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '《隐私协议》',
    tag: QuickLoginButtonComponent.PRIVACY_TAG,
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '和',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }, {
    text: '《华为账号用户认证协议》',
    tag: QuickLoginButtonComponent.USER_AUTHENTICATION_TAG,
    type: loginComponentManager.TextType.RICH_TEXT
  }, {
    text: '。',
    type: loginComponentManager.TextType.PLAIN_TEXT
  }];
  // 构造LoginWithHuaweiIDButton组件的控制器
  controller: loginComponentManager.LoginWithHuaweiIDButtonController =
    new loginComponentManager.LoginWithHuaweiIDButtonController()
      /**
       * 当应用使用自定义的登录页时，如果用户未同意协议，需要设置协议状态为NOT_ACCEPTED，当用户同意协议后再设置
       * 协议状态为ACCEPTED，才可以使用华为账号一键登录功能
       */
      .setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED)
      .onClickLoginWithHuaweiIDButton((error: BusinessError | undefined,
        response: loginComponentManager.HuaweiIDCredential) => {
        this.handleLoginWithHuaweiIDButton(error, response);
      })
      .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
        if (error) {
          this.dealAllError(error);
          return;
        }
        hilog.info(DOMAIN_ID, LOG_TAG, `onClickEvent clickEvent: ${clickEvent}`);
      });
  agreementDialog: CustomDialogController = new CustomDialogController({
    builder: AgreementDialog({
      privacyText: this.privacyText,
      cancel: () => {
        this.agreementDialog.close();
        this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED);
      },
      confirm: () => {
        this.agreementDialog.close();
        this.isSelected = true;
        this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
        // 调用此方法，同意协议与登录一并完成，无需再次点击登录按钮
        this.controller.continueLogin((error: BusinessError) => {
          if (error) {
            hilog.error(DOMAIN_ID, LOG_TAG,
              `Failed to login with agreementDialog. errCode is ${error.code}, errMessage is ${error.message}`);
          } else {
            hilog.info(DOMAIN_ID, LOG_TAG,
              'Succeed in clicking agreementDialog continueLogin.');
          }
        });
      },
      clickHyperlinkText: () => {
        this.agreementDialog.close();
        this.jumpToPrivacyWebView();
      }
    }),
    autoCancel: false,
    alignment: DialogAlignment.Center,
  });

  // Toast提示
  showToast(resource: string) {
    try {
      this.getUIContext().getPromptAction().showToast({
        message: resource,
        duration: 2000
      });
    } catch (error) {
      const message = (error as BusinessError).message;
      const code = (error as BusinessError).code;
      hilog.error(DOMAIN_ID, LOG_TAG, `showToast args  errCode is ${code}, errMessage is ${message}`);
    }
  }

  // 跳转华为账号用户认证协议页,该页面需在工程main_pages.json文件配置
  jumpToPrivacyWebView() {
    this.getUIContext().getRouter().pushUrl({
      // 在工程main_pages.json文件配置跳转页，具体可参考AccountKit开发指南使用华为账号一键登录WebPage示例代码
      url: 'pages/WebPage',
      params: {
        isFromDialog: true,
        url: QuickLoginButtonComponent.USER_AUTHENTICATION_PROTOCOL,
      }
    }, (err) => {
      if (err) {
        hilog.error(DOMAIN_ID, LOG_TAG,
          `Failed to jumpToPrivacyWebView, errCode is ${err.code}, errMessage is ${err.message}`);
      }
    });
  }

  handleLoginWithHuaweiIDButton(error: BusinessError | undefined,
    response: loginComponentManager.HuaweiIDCredential) {
    if (error) {
      hilog.error(DOMAIN_ID, LOG_TAG,
        `Failed to login with LoginWithHuaweiIDButton. errCode is ${error.code}, errMessage is ${error.message}`);
      if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
        this.getUIContext().showAlertDialog(
          {
            message: '网络未连接，请检查网络设置。',
            offset: { dx: 0, dy: -12 },
            alignment: DialogAlignment.Bottom,
            autoCancel: false,
            confirm: {
              value: '知道了',
              action: () => {
              }
            }
          }
        );
      } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
        // 未同意协议，弹出协议弹框，推荐使用该回调方式
        this.agreementDialog.open();
      } else if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
        // 华为账号未登录提示
        this.showToast('华为账号未登录，请重试');
      } else if (error.code === ErrorCode.ERROR_CODE_NOT_SUPPORTED) {
        // 不支持该scopes或permissions提示
        this.showToast('该scopes或permissions不支持');
      } else {
        // 其他提示系统或服务异常
        this.showToast('服务或网络异常，请稍后重试');
        // TODO: 其他错误码处理，请参考API中的错误码查看详细错误原因
      }
      return;
    }
    try {
      if (this.isSelected) {
        if (response) {
          hilog.info(DOMAIN_ID, LOG_TAG, 'Succeed in clicking LoginWithHuaweiIDButton.');
          // 开发者根据实际业务情况使用以下信息
          const authCode = response.authorizationCode;
          const openID = response.openID;
          const unionID = response.unionID;
          const idToken = response.idToken;
        }
      } else {
        this.agreementDialog.open();
      }
    } catch (err) {
      hilog.error(DOMAIN_ID, LOG_TAG,
        `Failed to login with LoginWithHuaweiIDButton, errCode: ${err.code}, errMessage: ${err.message}`);
      this.getUIContext().showAlertDialog(
        {
          message: '服务或网络异常，请稍后重试',
          offset: { dx: 0, dy: -12 },
          alignment: DialogAlignment.Bottom,
          autoCancel: false,
          confirm: {
            value: '知道了',
            action: () => {
            }
          }
        }
      );
    }
  }

  // 错误处理
  dealAllError(error: BusinessError): void {
    hilog.error(DOMAIN_ID, LOG_TAG,
      `Failed to login, errorCode is ${error.code}, errorMessage is ${error.message}`);
    // TODO: 错误码处理，请参考API中的错误码根据实际情况处理
  }

  build() {
    Scroll() {
      Column() {
        Column() {
          Column() {
            Image($r('sys.media.ohos_app_icon'))
              .width(48)
              .height(48)
              .draggable(false)
              .copyOption(CopyOptions.None)
              .onComplete(() => {
                hilog.info(DOMAIN_ID, LOG_TAG, 'appIcon loading success.');
              })
              .onError(() => {
                hilog.error(DOMAIN_ID, LOG_TAG, 'appIcon loading fail.');
              });

            Text($r('app.string.app_name'))
              .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
              .fontWeight(FontWeight.Medium)
              .fontWeight(FontWeight.Bold)
              .maxFontSize($r('sys.float.ohos_id_text_size_headline8'))
              .minFontSize($r('sys.float.ohos_id_text_size_body1'))
              .maxLines(1)
              .fontColor($r('sys.color.ohos_id_color_text_primary'))
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 12,
              });

            Text('应用描述')
              .fontSize($r('sys.float.ohos_id_text_size_body2'))
              .fontColor($r('sys.color.ohos_id_color_text_secondary'))
              .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
              .fontWeight(FontWeight.Regular)
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 8,
              });
          }.margin({
            top: 100
          });

          Column() {
            Text(this.quickLoginAnonymousPhone)
              .fontSize(36)
              .fontColor($r('sys.color.ohos_id_color_text_primary'))
              .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
              .fontWeight(FontWeight.Bold)
              .lineHeight(48)
              .textAlign(TextAlign.Center)
              .maxLines(1)
              .constraintSize({ maxWidth: '100%', minHeight: 48 });

            Text('华为账号绑定号码')
              .fontSize($r('sys.float.ohos_id_text_size_body2'))
              .fontColor($r('sys.color.ohos_id_color_text_secondary'))
              .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
              .fontWeight(FontWeight.Regular)
              .lineHeight(19)
              .textAlign(TextAlign.Center)
              .maxLines(1)
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 8
              });
          }.margin({
            top: 64
          });

          Column() {
            LoginWithHuaweiIDButton({
              params: {
                // LoginWithHuaweiIDButton支持的样式
                style: loginComponentManager.Style.BUTTON_RED,
                // 账号登录按钮在登录过程中展示加载态
                extraStyle: {
                  buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
                    show: true
                  })
                },
                // LoginWithHuaweiIDButton的边框圆角半径
                borderRadius: 24,
                // LoginWithHuaweiIDButton支持的登录类型
                loginType: loginComponentManager.LoginType.QUICK_LOGIN,
                // LoginWithHuaweiIDButton支持按钮的样式跟随系统深浅色模式切换
                supportDarkMode: true,
                // verifyPhoneNumber：如果华为账号用户在过去90天内未进行短信验证，是否拉起Account Kit提供的短信验证码页面
                verifyPhoneNumber: true
              },
              controller: this.controller
            });
          }
          .height(40)
          .margin({
            top: 56
          });

          Column() {
            Button({
              type: ButtonType.Capsule,
              stateEffect: true
            }) {
              Text('其他方式登录')
                .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
                .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
                .fontWeight(FontWeight.Medium)
                .fontSize($r('sys.float.ohos_id_text_size_button1'))
                .focusable(true)
                .focusOnTouch(true)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
                .maxLines(1)
                .padding({ left: 8, right: 8 });
            }
            .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
            .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
            .fontWeight(FontWeight.Medium)
            .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
            .focusable(true)
            .focusOnTouch(true)
            .constraintSize({ minHeight: 40 })
            .width('100%')
            .onClick(() => {
              hilog.info(DOMAIN_ID, LOG_TAG, 'click optionalLoginButton.');
            });
          }.margin({ top: 16 });
        }.width('100%');

        Row() {
          Row() {
            Checkbox({ name: 'privacyCheckbox', group: 'privacyCheckboxGroup' })
              .width(24)
              .height(24)
              .focusable(true)
              .focusOnTouch(true)
              .margin({ top: 0 })
              .select(this.isSelected)
              .onChange((value: boolean) => {
                if (value) {
                  this.isSelected = true;
                  this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
                } else {
                  this.isSelected = false;
                  this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED);
                }
                hilog.info(DOMAIN_ID, LOG_TAG, `agreementChecked: ${value}`);
              });
          };

          Row() {
            Text() {
              ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
                if (item?.type == loginComponentManager.TextType.PLAIN_TEXT && item?.text) {
                  Span(item?.text)
                    .fontColor($r('sys.color.ohos_id_color_text_secondary'))
                    .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
                    .fontWeight(FontWeight.Regular)
                    .fontSize($r('sys.float.ohos_id_text_size_body3'));
                } else if (item?.type == loginComponentManager.TextType.RICH_TEXT && item?.text) {
                  Span(item?.text)
                    .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
                    .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
                    .fontWeight(FontWeight.Medium)
                    .fontSize($r('sys.float.ohos_id_text_size_body3'))
                    .focusable(true)
                    .focusOnTouch(true)
                    .onClick(() => {
                      // 应用需要根据item.tag实现协议页面的跳转逻辑
                      hilog.info(DOMAIN_ID, LOG_TAG, `click privacy text tag: ${item.tag}`);
                      // 华为账号用户认证协议
                      if (item.tag === QuickLoginButtonComponent.USER_AUTHENTICATION_TAG) {
                        this.jumpToPrivacyWebView();
                      }
                    });
                }
              }, (item: loginComponentManager.PrivacyText, index: number) => {
                return item?.tag + index.toString();
              });
            }
            .width('100%');
          }
          .margin({ left: 12 })
          .layoutWeight(1)
          .constraintSize({ minHeight: 24 });
        }
        .alignItems(VerticalAlign.Top)
        .margin({
          bottom: 16,
          top: 16
        });
      }
      .justifyContent(FlexAlign.SpaceBetween)
      .constraintSize({ minHeight: '100%' })
      .margin({
        left: 16,
        right: 16
      });
    }
    .width('100%')
    .height('100%');
  }
}

@CustomDialog
export struct AgreementDialog {
  logTag: string = 'AgreementDialog';
  domainId: number = 0x0000;
  dialogController?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };
  clickHyperlinkText: () => void = () => {
  };
  privacyText: loginComponentManager.PrivacyText[] = [];
  private static USER_AUTHENTICATION_TAG = '华为账号用户认证协议';

  build() {
    Column() {
      Row() {
        Text('用户协议与隐私条款')
          .id('loginPanel_agreement_dialog_privacy_title')
          .maxFontSize($r('sys.float.ohos_id_text_size_headline8'))
          .minFontSize($r('sys.float.ohos_id_text_size_body1'))
          .fontColor($r('sys.color.ohos_id_color_text_primary'))
          .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .maxLines(2);
      }
      .alignItems(VerticalAlign.Center)
      .constraintSize({ minHeight: 56, maxWidth: 400 })
      .margin({
        left: $r('sys.float.ohos_id_max_padding_start'),
        right: $r('sys.float.ohos_id_max_padding_start')
      });

      Row() {
        Text() {
          ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
            if (item?.type == loginComponentManager.TextType.PLAIN_TEXT && item?.text) {
              Span(item?.text)
                .fontSize($r('sys.float.ohos_id_text_size_body1'))
                .fontColor($r('sys.color.ohos_id_color_text_primary'))
                .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
                .fontWeight(FontWeight.Regular);
            } else if (item?.type == loginComponentManager.TextType.RICH_TEXT && item?.text) {
              Span(item?.text)
                .fontSize($r('sys.float.ohos_id_text_size_body1'))
                .fontColor('#CE0E2D')
                .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
                .fontWeight(FontWeight.Medium)
                .focusable(true)
                .focusOnTouch(true)
                .onClick(() => {
                  // 应用需要根据item.tag实现协议页面的跳转逻辑
                  hilog.info(this.domainId, this.logTag, `click privacy text tag: ${item.tag}`);
                  // 华为账号用户认证协议
                  if (item.tag === AgreementDialog.USER_AUTHENTICATION_TAG) {
                    hilog.info(this.domainId, this.logTag, 'AgreementDialog click.');
                    this.clickHyperlinkText();
                  }
                });
            }
          }, (item: loginComponentManager.PrivacyText, index: number) => {
            return item?.tag + index.toString();
          });
        }
        .width('100%')
        .textOverflow({ overflow: TextOverflow.Ellipsis })
        .maxLines(10)
        .textAlign(TextAlign.Start)
        .focusable(true)
        .focusOnTouch(true)
        .padding({ left: 24, right: 24 });
      }.width('100%');

      Flex({
        direction: FlexDirection.Row
      }) {
        Button('取消',
          { type: ButtonType.Capsule, stateEffect: true })
          .id('loginPanel_agreement_cancel_btn')
          .fontColor($r('sys.color.ohos_id_color_text_primary'))
          .fontSize($r('sys.float.ohos_id_text_size_button1'))
          .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
          .backgroundColor(Color.Transparent)
          .fontWeight(FontWeight.Medium)
          .focusable(true)
          .focusOnTouch(true)
          .constraintSize({ minHeight: 40, maxWidth: 400 })
          .width('50%')
          .onClick(() => {
            hilog.info(this.domainId, this.logTag, 'AgreementDialog cancel.');
            this.cancel();
          });

        Button('同意并登录',
          { type: ButtonType.Capsule, stateEffect: true })
          .id('loginPanel_agreement_dialog_huawei_id_login_btn')
          .fontColor(Color.White)
          .backgroundColor('#CE0E2D')
          .fontSize($r('sys.float.ohos_id_text_size_button1'))
          .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
          .fontWeight(FontWeight.Medium)
          .focusable(true)
          .focusOnTouch(true)
          .constraintSize({ minHeight: 40, maxWidth: 400 })
          .width('50%')
          .onClick(() => {
            hilog.info(this.domainId, this.logTag, 'AgreementDialog confirm.');
            this.confirm();
          });
      }
      .margin({
        top: 8,
        left: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
        right: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
        bottom: 16
      });
    }.backgroundColor($r('sys.color.ohos_id_color_dialog_default_bg'))
    .padding({
      left: 16,
      right: 16
    });
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 该账号不支持一键登录，如儿童账号、海外账号
  ERROR_CODE_NOT_SUPPORTED = 1001500003,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 用户未同意用户协议
  ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001
}
```

## 总结

LoginWithHuaweiIDButton组件的类型是在初始化时由loginType类型决定，不支持动态改变，可通过条件渲染的方式来满足动态切换登录类型的需求。
