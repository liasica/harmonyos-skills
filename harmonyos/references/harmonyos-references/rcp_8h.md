---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h
title: rcp.h
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 头文件 > rcp.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:57+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:51bd712050698b692f9e978aa81fb28cf438788f5a1a5275f611773ec20212a7
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于访问远程通信的API。提供基本的函数，结构体和const定义。

**引用文件：** <RemoteCommunicationKit/rcp.h>

**库：** librcp\_c.so

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| struct [Rcp\_Buffer](_rcp___buffer.md) | 文本存储结构。 |
| struct [Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md) | [Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md)中使用的简单表单数据字段值。 |
| struct [Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md) | 表单字段文件值。 |
| struct [Rcp\_FormFieldValue](_rcp___form_field_value.md) | 简单表单数据字段值，参见[Rcp\_Form](remote-communication-overview.md#rcp_form)和[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)。 |
| struct [Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md) | 多部分表单域值，在[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)中使用。 |
| struct [Rcp\_RequestContent](_rcp___request_content.md) | 请求的内容。 |
| struct [Rcp\_HeaderValue](_rcp___header_value.md) | 请求或响应的标头映射的值类型。 |
| struct [Rcp\_HeaderEntry](_rcp___header_entry.md) | 请求或响应的标头的所有键值对。 |
| struct [Rcp\_Credential](_rcp___credential.md) | 服务器身份验证中使用的身份验证凭据，包括用户名和密码。 |
| struct [Rcp\_ServerAuthentication](_rcp___server_authentication.md) | 服务器身份验证。 |
| struct [Rcp\_Urls](_rcp___urls.md) | url，用于确定主机是否正在使用代理。 |
| struct [Rcp\_Exclusions](_rcp___exclusions.md) | 代理配置中用于过滤不使用代理的urls。 |
| struct [Rcp\_CertificateAuthority](_rcp___certificate_authority.md) | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| struct [Rcp\_ClientCertificate](_rcp___client_certificate.md) | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| struct [Rcp\_SecurityConfiguration](_rcp___security_configuration.md) | 请求的安全配置。 |
| struct [Rcp\_WebProxy](_rcp___web_proxy.md) | 自定义代理配置。 |
| struct [Rcp\_IpAndPort](_rcp___ip_and_port.md) | 该接口用在[Rcp\_DnsServers](_rcp___dns_servers.md)中，表示一个DNS服务器的地址和端口。 |
| struct [Rcp\_DnsServers](_rcp___dns_servers.md) | DNS服务器。[Rcp\_DnsConfiguration.dnsRules](_rcp___dns_configuration.md#dnsrules)中的类型之一。 |
| struct [Rcp\_IpAddress](_rcp___ip_address.md) | 指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](_rcp___static_dns_rule_item.md)。 |
| struct [Rcp\_StaticDnsRuleItem](_rcp___static_dns_rule_item.md) | 描述单个静态DNS规则。 |
| struct [Rcp\_StaticDnsRule](_rcp___static_dns_rule.md) | 静态DNS规则。 |
| struct [Rcp\_DnsRule](_rcp___dns_rule.md) | DNS规则配置。 |
| struct [Rcp\_OnDataReceiveCallback](_rcp___on_data_receive_callback.md) | 接收到数据时回调。[Rcp\_EventsHandler](_rcp___events_handler.md)中的配置。 |
| struct [Rcp\_OnProgressCallback](_rcp___on_progress_callback.md) | 收发时回调配置，在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置。 |
| struct [Rcp\_OnHeaderReceiveCallback](_rcp___on_header_receive_callback.md) | [Rcp\_EventsHandler](_rcp___events_handler.md)中配置的接收到的header的回调配置。 |
| struct [Rcp\_OnVoidCallback](_rcp___on_void_callback.md) | 在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置的数据结束或已取消事件的回调配置。 |
| struct [Rcp\_EventsHandler](_rcp___events_handler.md) | 监听不同HTTP事件的回调函数。 |
| struct [Rcp\_Timeout](_rcp___timeout.md) | 请求的超时配置 |
| struct [Rcp\_DnsOverHttps](_rcp___dns_over_https.md) | HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。 |
| struct [Rcp\_TransferConfiguration](_rcp___transfer_configuration.md) | 传输配置。 |
| struct [Rcp\_InfoToCollect](_rcp___info_to_collect.md) | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| struct [Rcp\_TracingConfiguration](_rcp___tracing_configuration.md) | 请求追踪配置。 |
| struct [Rcp\_ProxyConfiguration](_rcp___proxy_configuration.md) | 代理配置。 |
| struct [Rcp\_DnsConfiguration](_rcp___dns_configuration.md) | DNS解析配置。 |
| struct [Rcp\_Configuration](_rcp___configuration.md) | 请求配置。 |
| struct [Rcp\_TransferRange](_rcp___transfer_range.md) | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。 |
| struct [Rcp\_Request](_rcp___request.md) | 网络请求。 |
| struct [Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md) | 描述请求的所有Cookie键值对。 |
| struct [Rcp\_DebugInfo](_rcp___debug_info.md) | 描述存储在[Rcp\_Response](_rcp___response.md)中的调试信息的结构。 |
| struct [Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md) | 响应Cookie属性条目。 |
| struct [Rcp\_ResponseCookies](_rcp___response_cookies.md) | 响应Cookie。 |
| struct [Rcp\_TimeInfo](_rcp___time_info.md) | 响应计时信息。 |
| struct [Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md) | 响应回调结构体。 |
| struct [Rcp\_Response](_rcp___response.md) | 网络请求的响应。 |
| struct [Rcp\_Interceptor](_rcp___interceptor.md) | 异步拦截器。 |
| struct [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md) | 同步拦截器 |
| struct [Rcp\_InterceptorArray](_rcp___interceptor_array.md) | 异步拦截器数组。 |
| struct [Rcp\_SyncInterceptorArray](_rcp___sync_interceptor_array.md) | 同步拦截器数组。 |
| struct [Rcp\_SessionListener](_rcp___session_listener.md) | 关闭或取消会话事件的回调函数。 |
| struct [Rcp\_ConnectionConfiguration](_rcp___connection_configuration.md) | 连接配置。 |
| struct [Rcp\_SessionConfiguration](_rcp___session_configuration.md) | 会话配置。 |
| struct [Rcp\_OnBinaryReceiveCallback](_rcp___on_binary_receive_callback.md) | 接收到响应数据时的回调。支持二进制数据的接收。使用[HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](remote-communication-overview.md#hms_rcp_setrequestonbinarydatarecvcallback)给请求设置。 |
| struct [Rcp\_OnStatusCodeReceiveCallback](_rcp___on_status_code_callback.md) | 接收到响应状态码时的回调。使用[HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](remote-communication-overview.md#hms_rcp_setrequestonstatuscodereceivecallback)给请求设置。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [RCP\_MAX\_REQUEST\_ID\_LEN](remote-communication-overview.md#rcp_max_request_id_len) 32 | 请求ID的最大长度。 |
| [RCP\_MAX\_CONTENT\_TYPE\_LEN](remote-communication-overview.md#rcp_max_content_type_len) 64 | 内容类型最大长度。 |
| [RCP\_MAX\_FILENAME\_LEN](remote-communication-overview.md#rcp_max_filename_len) 128 | 文件名最大长度。 |
| [RCP\_MAX\_PATH\_LEN](remote-communication-overview.md#rcp_max_path_len) 128 | 路径的最大长度。 |
| [RCP\_METHOD\_GET](remote-communication-overview.md#rcp_method_get) "GET" | HTTP get方法。 |
| [RCP\_METHOD\_HEAD](remote-communication-overview.md#rcp_method_head) "HEAD" | HTTP head方法。 |
| [RCP\_METHOD\_OPTIONS](remote-communication-overview.md#rcp_method_options) "OPTIONS" | HTTP options方法。 |
| [RCP\_METHOD\_TRACE](remote-communication-overview.md#rcp_method_trace) "TRACE" | HTTP trace方法。 |
| [RCP\_METHOD\_DELETE](remote-communication-overview.md#rcp_method_delete) "DELETE" | HTTP delete方法。 |
| [RCP\_METHOD\_POST](remote-communication-overview.md#rcp_method_post) "POST" | HTTP post方法。 |
| [RCP\_METHOD\_PUT](remote-communication-overview.md#rcp_method_put) "PUT" | HTTP put方法。 |
| [RCP\_METHOD\_PATCH](remote-communication-overview.md#rcp_method_patch) "PATCH" | HTTP patch方法。 |
| [RCP\_IP\_MAX\_LEN](remote-communication-overview.md#rcp_ip_max_len) 40 | IP地址的最大长度。 |
| [RCP\_HOST\_MAX\_LEN](remote-communication-overview.md#rcp_host_max_len) 256 | 主机名的最大长度。 |

### 类型定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| typedef enum [Rcp\_FormValueType](remote-communication-overview.md#rcp_formvaluetype)[Rcp\_FormValueType](remote-communication-overview.md#rcp_formvaluetype) | 表单值类型。 |
| typedef int(\* [Rcp\_GetDataCallback](remote-communication-overview.md#rcp_getdatacallback)) (char \*out, uint32\_t size) | 通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。 |
| typedef enum [Rcp\_ContentOrPathOrCallbackType](remote-communication-overview.md#rcp_contentorpathorcallbacktype)[Rcp\_ContentOrPathOrCallbackType](remote-communication-overview.md#rcp_contentorpathorcallbacktype) | 回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md)中使用的数据。 |
| typedef struct [Rcp\_Buffer](_rcp___buffer.md)[Rcp\_Buffer](remote-communication-overview.md#rcp_buffer) | 文本存储结构。 |
| typedef struct [Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md)[Rcp\_ContentOrPathOrCallback](remote-communication-overview.md#rcp_contentorpathorcallback) | [Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md)中使用的简单表单数据字段值。 |
| typedef enum [Rcp\_MultipartValueType](remote-communication-overview.md#rcp_multipartvaluetype)[Rcp\_MultipartValueType](remote-communication-overview.md#rcp_multipartvaluetype) | 多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)中使用的数据。 |
| typedef struct [Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md)[Rcp\_FormFieldFileValue](remote-communication-overview.md#rcp_formfieldfilevalue) | 表单字段文件值。 |
| typedef struct [Rcp\_FormFieldValue](_rcp___form_field_value.md)[Rcp\_FormFieldValue](remote-communication-overview.md#rcp_formfieldvalue) | 简单表单数据字段值，参见[Rcp\_Form](remote-communication-overview.md#rcp_form)和[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)。 |
| typedef struct [Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)[Rcp\_MultipartFormFieldValue](remote-communication-overview.md#rcp_multipartformfieldvalue) | 多部分表单域值，在[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)中使用。 |
| typedef enum [Rcp\_ContentType](remote-communication-overview.md#rcp_contenttype)[Rcp\_ContentType](remote-communication-overview.md#rcp_contenttype) | 内容类型。用于区分[Rcp\_RequestContent](_rcp___request_content.md)中使用的数据。 |
| typedef struct [Rcp\_Form](remote-communication-overview.md#rcp_form)[Rcp\_Form](remote-communication-overview.md#rcp_form) | 简单表单。 |
| typedef struct [Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform) | 多部分表单。 |
| typedef struct [Rcp\_RequestContent](_rcp___request_content.md)[Rcp\_RequestContent](remote-communication-overview.md#rcp_requestcontent) | 请求的内容。 |
| typedef struct [Rcp\_Headers](remote-communication-overview.md#rcp_headers)[Rcp\_Headers](remote-communication-overview.md#rcp_headers) | 请求或响应的标头。 |
| typedef struct [Rcp\_HeaderValue](_rcp___header_value.md)[Rcp\_HeaderValue](remote-communication-overview.md#rcp_headervalue) | 请求或响应的标头映射的值类型。 |
| typedef struct [Rcp\_HeaderEntry](_rcp___header_entry.md)[Rcp\_HeaderEntry](remote-communication-overview.md#rcp_headerentry) | 请求或响应的标头的所有键值对。 |
| typedef enum [Rcp\_AuthenticationType](remote-communication-overview.md#rcp_authenticationtype)[Rcp\_AuthenticationType](remote-communication-overview.md#rcp_authenticationtype) | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| typedef struct [Rcp\_Credential](_rcp___credential.md)[Rcp\_Credential](remote-communication-overview.md#rcp_credential) | 服务器身份验证中使用的身份验证凭据，包括用户名和密码。 |
| typedef struct [Rcp\_ServerAuthentication](_rcp___server_authentication.md)[Rcp\_ServerAuthentication](remote-communication-overview.md#rcp_serverauthentication) | 服务器身份验证。 |
| typedef bool(\* [Rcp\_ExclusionFunction](remote-communication-overview.md#rcp_exclusionfunction)) (const char \*url) | 判断host是否使用代理的函数指针。 |
| typedef struct [Rcp\_Urls](_rcp___urls.md)[Rcp\_Urls](remote-communication-overview.md#rcp_urls) | url，用于确定主机是否正在使用代理。 |
| typedef enum [Rcp\_ExclusionsValueType](remote-communication-overview.md#rcp_exclusionsvaluetype)[Rcp\_ExclusionsValueType](remote-communication-overview.md#rcp_exclusionsvaluetype) | 代理排除中使用的数据类型. 用于区分[Rcp\_Exclusions](_rcp___exclusions.md)中使用的数据。 |
| typedef struct [Rcp\_Exclusions](_rcp___exclusions.md)[Rcp\_Exclusions](remote-communication-overview.md#rcp_exclusions) | 代理配置中用于过滤不使用代理的URLs。 |
| typedef enum [Rcp\_CertType](remote-communication-overview.md#rcp_certtype)[Rcp\_CertType](remote-communication-overview.md#rcp_certtype) | 客户端证书类型。 |
| typedef struct [Rcp\_CertificateAuthority](_rcp___certificate_authority.md)[Rcp\_CertificateAuthority](remote-communication-overview.md#rcp_certificateauthority) | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| typedef struct [Rcp\_ClientCertificate](_rcp___client_certificate.md)[Rcp\_ClientCertificate](remote-communication-overview.md#rcp_clientcertificate) | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| typedef enum [Rcp\_RemoteValidationType](remote-communication-overview.md#rcp_remotevalidationtype)[Rcp\_RemoteValidationType](remote-communication-overview.md#rcp_remotevalidationtype) | 远程验证类型。 |
| typedef struct [Rcp\_SecurityConfiguration](_rcp___security_configuration.md)[Rcp\_SecurityConfiguration](remote-communication-overview.md#rcp_securityconfiguration) | 请求的安全配置。 |
| typedef enum [Rcp\_ProxyTunnelMode](remote-communication-overview.md#rcp_proxytunnelmode)[Rcp\_ProxyTunnelMode](remote-communication-overview.md#rcp_proxytunnelmode) | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道。“always”表示始终创建隧道。 |
| typedef struct [Rcp\_WebProxy](_rcp___web_proxy.md)[Rcp\_WebProxy](remote-communication-overview.md#rcp_webproxy) | 自定义代理配置。 |
| typedef struct [Rcp\_IpAndPort](_rcp___ip_and_port.md)[Rcp\_IpAndPort](remote-communication-overview.md#rcp_ipandport) | 该接口用在[Rcp\_DnsServers](_rcp___dns_servers.md)中，表示一个DNS服务器的地址和端口。 |
| typedef struct [Rcp\_DnsServers](_rcp___dns_servers.md)[Rcp\_DnsServers](remote-communication-overview.md#rcp_dnsservers) | DNS服务器。[Rcp\_DnsConfiguration.dnsRules](_rcp___dns_configuration.md#dnsrules)中的类型之一。 |
| typedef struct [Rcp\_IpAddress](_rcp___ip_address.md)[Rcp\_IpAddress](remote-communication-overview.md#rcp_ipaddress) | 指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](_rcp___static_dns_rule_item.md)。 |
| typedef struct [Rcp\_StaticDnsRuleItem](_rcp___static_dns_rule_item.md)[Rcp\_StaticDnsRuleItem](remote-communication-overview.md#rcp_staticdnsruleitem) | 描述单个静态DNS规则。 |
| typedef struct [Rcp\_StaticDnsRule](_rcp___static_dns_rule.md)[Rcp\_StaticDnsRule](remote-communication-overview.md#rcp_staticdnsrule) | 静态DNS规则。 |
| typedef [Rcp\_IpAddress](_rcp___ip_address.md) \*(\* [Rcp\_DynamicDnsRuleFunction](remote-communication-overview.md#rcp_dynamicdnsrulefunction)) (const char \*host, uint16\_t port) | 一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。 |
| typedef enum [Rcp\_DnsRuleType](remote-communication-overview.md#rcp_dnsruletype)[Rcp\_DnsRuleType](remote-communication-overview.md#rcp_dnsruletype) | DNS规则类型。用于区分[Rcp\_DnsRule](_rcp___dns_rule.md)中使用的dns规则类型。 |
| typedef struct [Rcp\_DnsRule](_rcp___dns_rule.md)[Rcp\_DnsRule](remote-communication-overview.md#rcp_dnsrule) | DNS规则配置。 |
| typedef size\_t(\* [Rcp\_OnDataReceiveCallbackFunc](remote-communication-overview.md#rcp_ondatareceivecallbackfunc)) (void \*usrObject, const char \*data) | 接收到响应正文时调用的回调函数。 |
| typedef size\_t(\* [Rcp\_OnBinaryReceiveCallbackFunc](remote-communication-overview.md#rcp_onbinaryreceivecallbackfunc)) (void \*usrObject, [Rcp\_Buffer](_rcp___buffer.md) \*buffer) | 接收到响应正文时调用的回调函数（二进制数据）。 |
| typedef void (\* [Rcp\_OnStatusCodeReceiveCallbackFunc](remote-communication-overview.md#rcp_onstatuscodereceivecallbackfunc))(void \*usrObject, uint32\_t statusCode) | 接收到响应状态码时调用的回调函数。 |
| typedef void(\* [Rcp\_OnProgressCallbackFunc](remote-communication-overview.md#rcp_onprogresscallbackfunc)) (void \*usrObject, uint64\_t totalSize, uint64\_t transferredSize) | 请求/响应数据传输过程中调用的回调函数。 |
| typedef void(\* [Rcp\_OnHeaderReceiveCallbackFunc](remote-communication-overview.md#rcp_onheaderreceivecallbackfunc)) (void \*usrObject, [Rcp\_Headers](remote-communication-overview.md#rcp_headers) \*headers) | 收到所有请求时调用的回调。 |
| typedef void(\* [Rcp\_OnVoidCallbackFunc](remote-communication-overview.md#rcp_onvoidcallbackfunc)) (void \*usrObject) | 请求的DataEnd或Canceled事件回调的回调函数。 |
| typedef struct [Rcp\_OnDataReceiveCallback](_rcp___on_data_receive_callback.md)[Rcp\_OnDataReceiveCallback](remote-communication-overview.md#rcp_ondatareceivecallback) | 接收到数据时回调。[Rcp\_EventsHandler](_rcp___events_handler.md)中的配置。 |
| typedef struct [Rcp\_OnProgressCallback](_rcp___on_progress_callback.md)[Rcp\_OnProgressCallback](remote-communication-overview.md#rcp_onprogresscallback) | 收发时回调配置，在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置。 |
| typedef struct [Rcp\_OnHeaderReceiveCallback](_rcp___on_header_receive_callback.md)[Rcp\_OnHeaderReceiveCallback](remote-communication-overview.md#rcp_onheaderreceivecallback) | [Rcp\_EventsHandler](_rcp___events_handler.md)中配置的接收到的header的回调配置。 |
| typedef struct [Rcp\_OnVoidCallback](_rcp___on_void_callback.md)[Rcp\_OnVoidCallback](remote-communication-overview.md#rcp_onvoidcallback) | 在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置的数据结束或已取消事件的回调配置。 |
| typedef struct [Rcp\_EventsHandler](_rcp___events_handler.md)[Rcp\_EventsHandler](remote-communication-overview.md#rcp_eventshandler) | 监听不同HTTP事件的回调函数。 |
| typedef struct [Rcp\_Timeout](_rcp___timeout.md)[Rcp\_Timeout](remote-communication-overview.md#rcp_timeout) | 请求的超时配置。 |
| typedef struct [Rcp\_DnsOverHttps](_rcp___dns_over_https.md)[Rcp\_DnsOverHttps](remote-communication-overview.md#rcp_dnsoverhttps) | HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。 |
| typedef enum [Rcp\_PathPreference](remote-communication-overview.md#rcp_pathpreference)[Rcp\_PathPreference](remote-communication-overview.md#rcp_pathpreference) | 请求路径首选项。 |
| typedef struct [Rcp\_TransferConfiguration](_rcp___transfer_configuration.md)[Rcp\_TransferConfiguration](remote-communication-overview.md#rcp_transferconfiguration) | 传输配置。 |
| typedef struct [Rcp\_InfoToCollect](_rcp___info_to_collect.md)[Rcp\_InfoToCollect](remote-communication-overview.md#rcp_infotocollect) | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| typedef struct [Rcp\_TracingConfiguration](_rcp___tracing_configuration.md)[Rcp\_TracingConfiguration](remote-communication-overview.md#rcp_tracingconfiguration) | 请求追踪配置。 |
| typedef enum [Rcp\_ProxyType](remote-communication-overview.md#rcp_proxytype)[Rcp\_ProxyType](remote-communication-overview.md#rcp_proxytype) | 代理类型。用于区分不同的代理配置。 |
| typedef struct [Rcp\_ProxyConfiguration](_rcp___proxy_configuration.md)[Rcp\_ProxyConfiguration](remote-communication-overview.md#rcp_proxyconfiguration) | 代理配置。 |
| typedef struct [Rcp\_DnsConfiguration](_rcp___dns_configuration.md)[Rcp\_DnsConfiguration](remote-communication-overview.md#rcp_dnsconfiguration) | DNS解析配置。 |
| typedef struct [Rcp\_Configuration](_rcp___configuration.md)[Rcp\_Configuration](remote-communication-overview.md#rcp_configuration) | 请求配置。 |
| typedef struct [Rcp\_TransferRange](_rcp___transfer_range.md)[Rcp\_TransferRange](remote-communication-overview.md#rcp_transferrange) | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。 |
| typedef struct [Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies)[Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies) | 请求Cookie。 |
| typedef struct [Rcp\_Request](_rcp___request.md)[Rcp\_Request](remote-communication-overview.md#rcp_request) | 网络请求。 |
| typedef struct [Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md)[Rcp\_RequestCookieEntry](remote-communication-overview.md#rcp_requestcookieentry) | 描述请求的所有Cookie键值对。 |
| typedef enum [Rcp\_StatusCode](remote-communication-overview.md#rcp_statuscode)[Rcp\_StatusCode](remote-communication-overview.md#rcp_statuscode) | 请求响应的状态码。 |
| typedef enum [Rcp\_DebugEvent](remote-communication-overview.md#rcp_debugevent)[Rcp\_DebugEvent](remote-communication-overview.md#rcp_debugevent) | 描述调试信息的事件类型。 |
| typedef struct [Rcp\_DebugInfo](_rcp___debug_info.md)[Rcp\_DebugInfo](remote-communication-overview.md#rcp_debuginfo) | 描述存储在[Rcp\_Response](_rcp___response.md)中的调试信息的结构。 |
| typedef struct [Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes)[Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes) | 描述[Rcp\_Response](_rcp___response.md)中Cookie属性的类型。 |
| typedef struct [Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md)[Rcp\_CookieAttributeEntry](remote-communication-overview.md#rcp_cookieattributeentry) | 响应Cookie属性条目。 |
| typedef struct [Rcp\_ResponseCookies](_rcp___response_cookies.md)[Rcp\_ResponseCookies](remote-communication-overview.md#rcp_responsecookies) | 响应Cookie。 |
| typedef struct [Rcp\_TimeInfo](_rcp___time_info.md)[Rcp\_TimeInfo](remote-communication-overview.md#rcp_timeinfo) | 响应计时信息。 |
| typedef struct [Rcp\_Response](_rcp___response.md)[Rcp\_Response](remote-communication-overview.md#rcp_response) | 网络请求的响应。 |
| typedef void(\* [Rcp\_ResponseCallback](remote-communication-overview.md#rcp_responsecallback)) (void \*usrCtx, [Rcp\_Response](_rcp___response.md) \*response, uint32\_t errCode) | 响应回调函数指针。 |
| typedef struct [Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md)[Rcp\_ResponseCallbackObject](remote-communication-overview.md#rcp_responsecallbackobject) | 响应回调结构体。 |
| typedef struct [Rcp\_RequestHandler](remote-communication-overview.md#rcp_requesthandler)[Rcp\_RequestHandler](remote-communication-overview.md#rcp_requesthandler) | 与[Rcp\_Interceptor](_rcp___interceptor.md)关联的异步处理器。 |
| typedef struct [Rcp\_SyncRequestHandler](remote-communication-overview.md#rcp_syncrequesthandler)[Rcp\_SyncRequestHandler](remote-communication-overview.md#rcp_syncrequesthandler) | 与[Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)关联的同步处理器。 |
| typedef struct [Rcp\_Interceptor](_rcp___interceptor.md)[Rcp\_Interceptor](remote-communication-overview.md#rcp_interceptor) | 异步拦截器。 |
| typedef struct [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)[Rcp\_SyncInterceptor](remote-communication-overview.md#rcp_syncinterceptor) | 同步拦截器。 |
| typedef struct [Rcp\_InterceptorArray](_rcp___interceptor_array.md)[Rcp\_InterceptorArray](remote-communication-overview.md#rcp_interceptorarray) | 异步拦截器数组。 |
| typedef struct [Rcp\_SyncInterceptorArray](_rcp___sync_interceptor_array.md)[Rcp\_SyncInterceptorArray](remote-communication-overview.md#rcp_syncinterceptorarray) | 同步拦截器数组。 |
| typedef enum [Rcp\_SessionType](remote-communication-overview.md#rcp_sessiontype)[Rcp\_SessionType](remote-communication-overview.md#rcp_sessiontype) | 会话类型。 |
| typedef struct [Rcp\_Session](remote-communication-overview.md#rcp_session)[Rcp\_Session](remote-communication-overview.md#rcp_session) | 会话。 |
| typedef struct [Rcp\_SessionListener](_rcp___session_listener.md)[Rcp\_SessionListener](remote-communication-overview.md#rcp_sessionlistener) | 关闭或取消会话事件的回调函数。 |
| typedef struct [Rcp\_ConnectionConfiguration](_rcp___connection_configuration.md)[Rcp\_ConnectionConfiguration](remote-communication-overview.md#rcp_connectionconfiguration) | 连接配置。 |
| typedef struct [Rcp\_SessionConfiguration](_rcp___session_configuration.md)[Rcp\_SessionConfiguration](remote-communication-overview.md#rcp_sessionconfiguration) | 会话配置。 |
| typedef struct [Rcp\_OnBinaryReceiveCallback](_rcp___on_binary_receive_callback.md)[Rcp\_OnBinaryReceiveCallback](_rcp___on_binary_receive_callback.md) | 响应的二进制数据接收回调函数。 |
| typedef size\_t(\* [Rcp\_OnBinaryReceiveCallbackFunc](remote-communication-overview.md#rcp_onbinaryreceivecallbackfunc)) (void \*usrObject, [Rcp\_Buffer](_rcp___buffer.md) \*buffer) | 二进制数据接收回调函数指针。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_FormValueType](remote-communication-overview.md#rcp_formvaluetype) {  RCP\_FORM\_VALUE\_TYPE\_INT32, RCP\_FORM\_VALUE\_TYPE\_INT64, RCP\_FORM\_VALUE\_TYPE\_BOOL, RCP\_FORM\_VALUE\_TYPE\_STRING,  RCP\_FORM\_VALUE\_TYPE\_DOUBLE  } | 表单值类型。 |
| [Rcp\_ContentOrPathOrCallbackType](remote-communication-overview.md#rcp_contentorpathorcallbacktype) { RCP\_FILE\_VALUE\_TYPE\_CONTENT, RCP\_FILE\_VALUE\_TYPE\_PATH, RCP\_FILE\_VALUE\_TYPE\_CALLBACK} | 回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md)中使用的数据。 |
| [Rcp\_MultipartValueType](remote-communication-overview.md#rcp_multipartvaluetype) { RCP\_TYPE\_FORM\_FIELD\_VALUE, RCP\_TYPE\_FORM\_FIELD\_FILE\_VALUE } | 多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)中使用的数据。 |
| [Rcp\_ContentType](remote-communication-overview.md#rcp_contenttype) { RCP\_CONTENT\_TYPE\_STRING, RCP\_CONTENT\_TYPE\_FORM, RCP\_CONTENT\_TYPE\_MULTIPARTFORM, RCP\_CONTENT\_TYPE\_GETCALLBACK } | 内容类型。用于区分[Rcp\_RequestContent](_rcp___request_content.md)中使用的数据。 |
| [Rcp\_AuthenticationType](remote-communication-overview.md#rcp_authenticationtype) { RCP\_AUTHENTICATION\_AUTO, RCP\_AUTHENTICATION\_BASIC, RCP\_AUTHENTICATION\_NTLM, RCP\_AUTHENTICATION\_DIGEST } | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| [Rcp\_ExclusionsValueType](remote-communication-overview.md#rcp_exclusionsvaluetype) { RCP\_EXCLUSION\_USE\_URL\_ARRAY, RCP\_EXCLUSION\_USE\_CALLBACK } | 代理排除中使用的数据类型. 用于区分[Rcp\_Exclusions](_rcp___exclusions.md)中使用的数据。 |
| [Rcp\_CertType](remote-communication-overview.md#rcp_certtype) { RCP\_CERT\_PEM, RCP\_CERT\_DER, RCP\_CERT\_P12 } | 客户端证书类型。 |
| [Rcp\_RemoteValidationType](remote-communication-overview.md#rcp_remotevalidationtype) { RCP\_REMOTE\_VALIDATION\_SYSTEM, RCP\_REMOTE\_VALIDATION\_SKIP, RCP\_REMOTE\_VALIDATION\_CERTIFICATE\_AUTHORITY } | 远程验证类型。 |
| [Rcp\_ProxyTunnelMode](remote-communication-overview.md#rcp_proxytunnelmode) { RCP\_PROXY\_TUNNEL\_AUTO, RCP\_PROXY\_TUNNEL\_ALWAYS } | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道。“always”表示始终创建隧道。 |
| [Rcp\_DnsRuleType](remote-communication-overview.md#rcp_dnsruletype) { RCP\_DNS\_RULE\_DNS\_SERVERS, RCP\_DNS\_RULE\_STATIC, RCP\_DNS\_RULE\_DYNAMIC } | DNS规则类型。用于区分[Rcp\_DnsRule](_rcp___dns_rule.md)中使用的dns规则类型。 |
| [Rcp\_PathPreference](remote-communication-overview.md#rcp_pathpreference) { RCP\_PATH\_PREFERENCE\_AUTO, RCP\_PATH\_PREFERENCE\_WIFI, RCP\_PATH\_PREFERENCE\_CELLULAR } | 请求路径首选项。 |
| [Rcp\_ProxyType](remote-communication-overview.md#rcp_proxytype) { RCP\_PROXY\_SYSTEM, RCP\_PROXY\_CUSTOM, RCP\_PROXY\_NO\_PROXY } | 代理类型。用于区分不同的代理配置。 |
| [Rcp\_StatusCode](remote-communication-overview.md#rcp_statuscode) {  RCP\_NONE = 0, RCP\_OK = 200, RCP\_CREATED, RCP\_ACCEPTED,  RCP\_NOT\_AUTHORITATIVE, RCP\_NO\_CONTENT, RCP\_RESET, RCP\_PARTIAL,  RCP\_MULTI\_CHOICE = 300, RCP\_MOVED\_PERMANENTLY, RCP\_MOVED\_TEMPORARILY, RCP\_SEE\_OTHER,  RCP\_NOT\_MODIFIED, RCP\_USE\_PROXY, RCP\_BAD\_REQUEST = 400, RCP\_UNAUTHORIZED,  RCP\_PAYMENT\_REQUIRED, RCP\_FORBIDDEN, RCP\_NOT\_FOUND, RCP\_BAD\_METHOD,  RCP\_NOT\_ACCEPTABLE, RCP\_PROXY\_AUTH, RCP\_CLIENT\_TIMEOUT, RCP\_CONFLICT,  RCP\_GONE, RCP\_LENGTH\_REQUIRED, RCP\_PRECON\_FAILED, RCP\_ENTITY\_TOO\_LARGE,  RCP\_REQ\_TOO\_LONG, RCP\_UNSUPPORTED\_TYPE, RCP\_INTERNAL\_ERROR = 500, RCP\_NOT\_IMPLEMENTED,  RCP\_BAD\_GATEWAY, RCP\_UNAVAILABLE, RCP\_GATEWAY\_TIMEOUT, RCP\_VERSION  } | 请求响应的状态码。 |
| [Rcp\_DebugEvent](remote-communication-overview.md#rcp_debugevent) {  RCP\_DEBUG\_EVENT\_TEXT, RCP\_DEBUG\_EVENT\_HEADER\_IN, RCP\_DEBUG\_EVENT\_HEADER\_OUT, RCP\_DEBUG\_EVENT\_DATA\_IN,  RCP\_DEBUG\_EVENT\_DATA\_OUT, RCP\_DEBUG\_EVENT\_SSL\_DATA\_IN, RCP\_DEBUG\_EVENT\_SSL\_DATA\_OUT  } | 描述调试信息的事件类型。 |
| [Rcp\_SessionType](remote-communication-overview.md#rcp_sessiontype) { RCP\_SESSION\_TYPE\_HTTP = 0, RCP\_SESSION\_TYPE\_MAX = 100} | 会话类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_Form](remote-communication-overview.md#rcp_form) \* [HMS\_Rcp\_CreateForm](remote-communication-overview.md#hms_rcp_createform) (void) | 创建一个简单表单。 |
| void [HMS\_Rcp\_DestroyForm](remote-communication-overview.md#hms_rcp_destroyform) ([Rcp\_Form](remote-communication-overview.md#rcp_form) \*form) | 销毁一个简单表单。 |
| uint32\_t [HMS\_Rcp\_SetFormValue](remote-communication-overview.md#hms_rcp_setformvalue) ([Rcp\_Form](remote-communication-overview.md#rcp_form) \*form, const char \*key, const [Rcp\_FormFieldValue](_rcp___form_field_value.md) \*value) | 设置简单表单的键值对。 |
| [Rcp\_FormFieldValue](_rcp___form_field_value.md) \* [HMS\_Rcp\_GetFormValue](remote-communication-overview.md#hms_rcp_getformvalue) ([Rcp\_Form](remote-communication-overview.md#rcp_form) \*form, const char \*key) | 通过键获取一个简单表单的对应值。 |
| [Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform) \* [HMS\_Rcp\_CreateMultipartForm](remote-communication-overview.md#hms_rcp_createmultipartform) (void) | 创建一个多部分表单。 |
| void [HMS\_Rcp\_DestroyMultipartForm](remote-communication-overview.md#hms_rcp_destroymultipartform) ([Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform) \*multipartForm) | 销毁一个多部分表单。 |
| uint32\_t [HMS\_Rcp\_SetMultipartFormValue](remote-communication-overview.md#hms_rcp_setmultipartformvalue) ([Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform) \*multipartForm, const char \*key, const [Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md) \*value) | 设置多部分表单的键值对。 |
| [Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md) \* [HMS\_Rcp\_GetMultipartFormValue](remote-communication-overview.md#hms_rcp_getmultipartformvalue) ([Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform) \*multipartForm, const char \*key) | 通过键获取多部分表单的值。 |
| [Rcp\_Headers](remote-communication-overview.md#rcp_headers) \* [HMS\_Rcp\_CreateHeaders](remote-communication-overview.md#hms_rcp_createheaders) (void) | 为请求或响应创建标头。 |
| void [HMS\_Rcp\_DestroyHeaders](remote-communication-overview.md#hms_rcp_destroyheaders) ([Rcp\_Headers](remote-communication-overview.md#rcp_headers) \*headers) | 销毁请求或响应的标头。 |
| uint32\_t [HMS\_Rcp\_SetHeaderValue](remote-communication-overview.md#hms_rcp_setheadervalue) ([Rcp\_Headers](remote-communication-overview.md#rcp_headers) \*headers, const char \*name, const char \*value) | 设置请求或响应头的键值对。 |
| [Rcp\_HeaderValue](_rcp___header_value.md) \* [HMS\_Rcp\_GetHeaderValue](remote-communication-overview.md#hms_rcp_getheadervalue) ([Rcp\_Headers](remote-communication-overview.md#rcp_headers) \*headers, const char \*name) | 通过键获取请求或响应头的值。 |
| [Rcp\_HeaderEntry](_rcp___header_entry.md) \* [HMS\_Rcp\_GetHeaderEntries](remote-communication-overview.md#hms_rcp_getheaderentries) ([Rcp\_Headers](remote-communication-overview.md#rcp_headers) \*headers) | 获取请求或响应头的所有键值对。 |
| void [HMS\_Rcp\_DestroyHeaderEntries](remote-communication-overview.md#hms_rcp_destroyheaderentries) ([Rcp\_HeaderEntry](_rcp___header_entry.md) \*headerEntry) | 销毁[HMS\_Rcp\_GetHeaderEntries](remote-communication-overview.md#hms_rcp_getheaderentries)中获取的所有键值对。 |
| [Rcp\_Request](_rcp___request.md) \* [HMS\_Rcp\_CreateRequest](remote-communication-overview.md#hms_rcp_createrequest) (const char \*url) | 创建请求。 |
| void [HMS\_Rcp\_DestroyRequest](remote-communication-overview.md#hms_rcp_destroyrequest) ([Rcp\_Request](_rcp___request.md) \*request) | 销毁请求。 |
| [Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies) \* [HMS\_Rcp\_CreateRequestCookies](remote-communication-overview.md#hms_rcp_createrequestcookies) (void) | 创建空的请求Cookie。 |
| void [HMS\_Rcp\_DestroyRequestCookies](remote-communication-overview.md#hms_rcp_destroyrequestcookies) ([Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies) \*cookies) | 销毁请求Cookie。 |
| uint32\_t [HMS\_Rcp\_SetRequestCookieValue](remote-communication-overview.md#hms_rcp_setrequestcookievalue) ([Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies) \*cookies, const char \*name, const char \*value) | 设置请求Cookie。 |
| char \* [HMS\_Rcp\_GetRequestCookieValue](remote-communication-overview.md#hms_rcp_getrequestcookievalue) ([Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies) \*cookies, const char \*name) | 通过名称获取请求Cookie的值。 |
| [Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md) \* [HMS\_Rcp\_GetRequestCookieEntries](remote-communication-overview.md#hms_rcp_getrequestcookieentries) ([Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies) \*cookies) | 获取请求Cookie中的所有键值对。 |
| void [HMS\_Rcp\_DestroyRequestCookieEntries](remote-communication-overview.md#hms_rcp_destroyrequestcookieentries) ([Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md) \*cookieEntry) | 销毁从[HMS\_Rcp\_GetRequestCookieValue](remote-communication-overview.md#hms_rcp_getrequestcookievalue)获取的所有与请求Cookie相关的键值对。 |
| const char \* [HMS\_Rcp\_GetResponseCookieAttrValue](remote-communication-overview.md#hms_rcp_getresponsecookieattrvalue) ([Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes) \*cookieAttributes, const char \*name) | 通过名称获取Cookie属性的值。 |
| [Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md) \* [HMS\_Rcp\_GetResponseCookieAttrEntries](remote-communication-overview.md#hms_rcp_getresponsecookieattrentries) ([Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes) \*cookieAttributes) | 在[Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes)中获取所有响应Cookie属性。 |
| void [HMS\_Rcp\_DestroyResponseCookieAttrEntries](remote-communication-overview.md#hms_rcp_destroyresponsecookieattrentries) ([Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md) \*entries) | 销毁响应Cookie属性。 |
| uint32\_t [HMS\_Rcp\_CallNextRequestHandler](remote-communication-overview.md#hms_rcp_callnextrequesthandler) ([Rcp\_Request](_rcp___request.md) \*request, const [Rcp\_RequestHandler](remote-communication-overview.md#rcp_requesthandler) \*next, const [Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md) \*responseCallback) | 在拦截器[Rcp\_Interceptor](_rcp___interceptor.md)的函数中可以调用下一个拦截器或defaultHandler。 |
| [Rcp\_Response](_rcp___response.md) \* [HMS\_Rcp\_CallNextSyncRequestHandler](remote-communication-overview.md#hms_rcp_callnextsyncrequesthandler) ([Rcp\_Request](_rcp___request.md) \*request, const [Rcp\_SyncRequestHandler](remote-communication-overview.md#rcp_syncrequesthandler) \*next, uint32\_t \*errCode) | 在拦截器[Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)的函数中可以调用下一个拦截器或默认处理器。 |
| [Rcp\_Session](remote-communication-overview.md#rcp_session) \* [HMS\_Rcp\_CreateSession](remote-communication-overview.md#hms_rcp_createsession) (const [Rcp\_SessionConfiguration](_rcp___session_configuration.md) \*configuration, uint32\_t \*errCode) | 创建会话。 |
| const char \* [HMS\_Rcp\_GetSessionId](remote-communication-overview.md#hms_rcp_getsessionid) ([Rcp\_Session](remote-communication-overview.md#rcp_session) \*session) | 获取会话ID。 |
| const [Rcp\_SessionConfiguration](_rcp___session_configuration.md) \* [HMS\_Rcp\_GetSessionConfiguration](remote-communication-overview.md#hms_rcp_getsessionconfiguration) ([Rcp\_Session](remote-communication-overview.md#rcp_session) \*session) | 获取会话配置。 |
| [Rcp\_Response](_rcp___response.md) \* [HMS\_Rcp\_FetchSync](remote-communication-overview.md#hms_rcp_fetchsync) ([Rcp\_Session](remote-communication-overview.md#rcp_session) \*session, [Rcp\_Request](_rcp___request.md) \*request, uint32\_t \*errCode) | 发送同步请求并获取响应。 |
| uint32\_t [HMS\_Rcp\_Fetch](remote-communication-overview.md#hms_rcp_fetch) ([Rcp\_Session](remote-communication-overview.md#rcp_session) \*session, [Rcp\_Request](_rcp___request.md) \*request, const [Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md) \*responseCallback) | 发送异步请求并获取响应。 |
| uint32\_t [HMS\_Rcp\_CancelRequest](remote-communication-overview.md#hms_rcp_cancelrequest) ([Rcp\_Session](remote-communication-overview.md#rcp_session) \*session, const [Rcp\_Request](_rcp___request.md) \*request) | 取消一个请求。 |
| uint32\_t [HMS\_Rcp\_CancelSession](remote-communication-overview.md#hms_rcp_cancelsession) ([Rcp\_Session](remote-communication-overview.md#rcp_session) \*session) | 取消会话。 |
| uint32\_t [HMS\_Rcp\_CloseSession](remote-communication-overview.md#hms_rcp_closesession) ([Rcp\_Session](remote-communication-overview.md#rcp_session) \*\*session) | 关闭会话。 |
| uint32\_t [HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](remote-communication-overview.md#hms_rcp_setrequestonbinarydatarecvcallback) ([Rcp\_Request](_rcp___request.md) \*request, [Rcp\_OnBinaryReceiveCallback](_rcp___on_binary_receive_callback.md) onBinaryReceiveCallback) | 为请求设置流式接收二进制数据的回调函数。该回调函数与[Rcp\_OnDataReceiveCallback](_rcp___on_data_receive_callback.md)功能一致，功能上可以包含字符数据和二进制数据。 |
