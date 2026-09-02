---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview
title: RemoteCommunication
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 模块 > RemoteCommunication
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f775f1156f3593b16b08b63e6e31dc2c6aaa16943641d45a4166d3425d5dc377
---

## 概述

提供远程通信能力相关接口。

支持http会话功能。

**起始版本：** 5.0.0(12)

支持quic功能。

**起始版本：** 26.0.0

## 汇总

### 文件

| 名称 | 描述 |
| --- | --- |
| [rcp.h](rcp_8h.md) | 声明用于访问远程通信的API。提供基本的函数，结构体和const定义。 |
| [rcp\_quic.h](rcp_quic_h.md) | 声明quic协议相关的API。提供基本的函数，结构体和常量定义。 |

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [Rcp\_Buffer](_rcp___buffer.md) | 文本存储结构。 |
| struct [Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md) | [Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md)中使用的简单表单数据字段值。 |
| struct [Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md) | 表单字段文件值。 |
| struct [Rcp\_FormFieldValue](_rcp___form_field_value.md) | 简单表单数据字段值，参见[Rcp\_Form](remote-communication-overview.md#rcp_form)和[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)。 |
| struct [Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md) | 多部分表单域值，在[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)中使用。 |
| struct [Rcp\_FormOrder](_rcp___form_order.md) | 表单键值对发送顺序。 |
| struct [Rcp\_RequestContent](_rcp___request_content.md) | 请求的内容。 |
| struct [Rcp\_HeaderValue](_rcp___header_value.md) | 请求或响应的标头映射的值类型。 |
| struct [Rcp\_HeaderEntry](_rcp___header_entry.md) | 请求或响应的标头的所有键值对。 |
| struct [Rcp\_Credential](_rcp___credential.md) | 服务器身份验证中使用的身份验证凭据，包括用户名和密码。 |
| struct [Rcp\_ServerAuthentication](_rcp___server_authentication.md) | 服务器身份验证。 |
| struct [Rcp\_Urls](_rcp___urls.md) | URL，用于确定主机是否正在使用代理。 |
| struct [Rcp\_Exclusions](_rcp___exclusions.md) | 代理配置中用于过滤不使用代理的URLs。 |
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
| struct [Rcp\_OnVoidCallback](_rcp___on_void_callback.md) | 在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置的数据结束或取消事件的回调配置。 |
| struct [Rcp\_EventsHandler](_rcp___events_handler.md) | 监听不同HTTP事件的回调函数。 |
| struct [Rcp\_Timeout](_rcp___timeout.md) | 请求的超时配置。 |
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
| struct [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md) | 同步拦截器。 |
| struct [Rcp\_InterceptorArray](_rcp___interceptor_array.md) | 异步拦截器数组。 |
| struct [Rcp\_SyncInterceptorArray](_rcp___sync_interceptor_array.md) | 同步拦截器数组。 |
| struct [Rcp\_SessionListener](_rcp___session_listener.md) | 关闭或取消会话事件的回调函数。 |
| struct [Rcp\_ConnectionConfiguration](_rcp___connection_configuration.md) | 连接配置。 |
| struct [Rcp\_SessionConfiguration](_rcp___session_configuration.md) | 会话配置。 |
| struct [Rcp\_OnBinaryReceiveCallback](_rcp___on_binary_receive_callback.md) | 接收到响应的二进制数据时的回调。 |
| struct [Rcp\_OnStatusCodeReceiveCallback](_rcp___on_status_code_callback.md) | 接收到响应的状态码时的回调。 |
| struct [Rcp\_OnGetDataCallback](_rcp___on_get_data_callback.md) | 获取数据的回调。 |
| struct [Rcp\_QuicSlist](_rcp___quic_slist.md) | 链表数据结构。 |
| struct [Rcp\_QuicIpAddress](_rcp___quic_ipaddress.md) | 用于存储IP地址的数据结构。 |
| struct [Rcp\_QuicIoVec](_rcp___quic_io_vec.md) | 用于存储二进制内容的数据结构。 |
| struct [Rcp\_QuicStreamData](_rcp___quic_stream_data.md) | quic连接中用于接收流式数据的存储结构。 |

### 宏定义

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
| [RCP\_QUIC\_IP\_MAX\_LEN](remote-communication-overview.md#rcp_quic_ip_max_len) 40 | quic连接的IP地址的最大长度。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef enum [Rcp\_FormValueType](remote-communication-overview.md#rcp_formvaluetype) [Rcp\_FormValueType](remote-communication-overview.md#rcp_formvaluetype) | 表单值类型。 |
| typedef int(\* [Rcp\_GetDataCallback](remote-communication-overview.md#rcp_getdatacallback)) (char \*out, uint32\_t size) | 通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。 |
| typedef enum [Rcp\_ContentOrPathOrCallbackType](remote-communication-overview.md#rcp_contentorpathorcallbacktype) [Rcp\_ContentOrPathOrCallbackType](remote-communication-overview.md#rcp_contentorpathorcallbacktype) | 回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md)中使用的数据。 |
| typedef struct [Rcp\_Buffer](_rcp___buffer.md) [Rcp\_Buffer](remote-communication-overview.md#rcp_buffer) | 文本存储结构。 |
| typedef struct [Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md) [Rcp\_ContentOrPathOrCallback](remote-communication-overview.md#rcp_contentorpathorcallback) | [Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md)中使用的简单表单数据字段值。 |
| typedef enum [Rcp\_MultipartValueType](remote-communication-overview.md#rcp_multipartvaluetype) [Rcp\_MultipartValueType](remote-communication-overview.md#rcp_multipartvaluetype) | 多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)中使用的数据。 |
| typedef struct [Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md) [Rcp\_FormFieldFileValue](remote-communication-overview.md#rcp_formfieldfilevalue) | 表单字段文件值。 |
| typedef struct [Rcp\_FormFieldValue](_rcp___form_field_value.md) [Rcp\_FormFieldValue](remote-communication-overview.md#rcp_formfieldvalue) | 简单表单数据字段值，参见[Rcp\_Form](remote-communication-overview.md#rcp_form)和[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)。 |
| typedef struct [Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md) [Rcp\_MultipartFormFieldValue](remote-communication-overview.md#rcp_multipartformfieldvalue) | 多部分表单域值，在[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)中使用。 |
| typedef enum [Rcp\_ContentType](remote-communication-overview.md#rcp_contenttype) [Rcp\_ContentType](remote-communication-overview.md#rcp_contenttype) | 内容类型。用于区分[Rcp\_RequestContent](_rcp___request_content.md)中使用的数据。 |
| typedef struct [Rcp\_Form](remote-communication-overview.md#rcp_form) [Rcp\_Form](remote-communication-overview.md#rcp_form) | 简单表单。 |
| typedef struct [Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform) [Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform) | 多部分表单。 |
| typedef struct [Rcp\_FormOrder](_rcp___form_order.md) [Rcp\_FormOrder](remote-communication-overview.md#rcp_formorder) | 表单键值对发送顺序。 |
| typedef struct [Rcp\_RequestContent](_rcp___request_content.md) [Rcp\_RequestContent](remote-communication-overview.md#rcp_requestcontent) | 请求的内容。 |
| typedef struct [Rcp\_Headers](remote-communication-overview.md#rcp_headers) [Rcp\_Headers](remote-communication-overview.md#rcp_headers) | 请求或响应的标头。 |
| typedef struct [Rcp\_HeaderValue](_rcp___header_value.md) [Rcp\_HeaderValue](remote-communication-overview.md#rcp_headervalue) | 请求或响应的标头映射的值类型。 |
| typedef struct [Rcp\_HeaderEntry](_rcp___header_entry.md) [Rcp\_HeaderEntry](remote-communication-overview.md#rcp_headerentry) | 请求或响应的标头的所有键值对。 |
| typedef enum [Rcp\_AuthenticationType](remote-communication-overview.md#rcp_authenticationtype) [Rcp\_AuthenticationType](remote-communication-overview.md#rcp_authenticationtype) | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| typedef struct [Rcp\_Credential](_rcp___credential.md) [Rcp\_Credential](remote-communication-overview.md#rcp_credential) | 服务器身份验证中使用的身份验证凭据，包括用户名和密码。 |
| typedef struct [Rcp\_ServerAuthentication](_rcp___server_authentication.md) [Rcp\_ServerAuthentication](remote-communication-overview.md#rcp_serverauthentication) | 服务器身份验证。 |
| typedef bool(\* [Rcp\_ExclusionFunction](remote-communication-overview.md#rcp_exclusionfunction)) (const char \*url) | 判断host是否使用代理的函数指针，true代表使用，false代表不使用。 |
| typedef struct [Rcp\_Urls](_rcp___urls.md) [Rcp\_Urls](remote-communication-overview.md#rcp_urls) | url，用于确定主机是否正在使用代理。 |
| typedef enum [Rcp\_ExclusionsValueType](remote-communication-overview.md#rcp_exclusionsvaluetype) [Rcp\_ExclusionsValueType](remote-communication-overview.md#rcp_exclusionsvaluetype) | 代理排除中使用的数据类型，用于区分[Rcp\_Exclusions](_rcp___exclusions.md)中使用的数据。 |
| typedef struct [Rcp\_Exclusions](_rcp___exclusions.md) [Rcp\_Exclusions](remote-communication-overview.md#rcp_exclusions) | 代理配置中用于过滤不使用代理的URLs。 |
| typedef enum [Rcp\_CertType](remote-communication-overview.md#rcp_certtype) [Rcp\_CertType](remote-communication-overview.md#rcp_certtype) | 客户端证书类型。 |
| typedef struct [Rcp\_CertificateAuthority](_rcp___certificate_authority.md) [Rcp\_CertificateAuthority](remote-communication-overview.md#rcp_certificateauthority) | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| typedef struct [Rcp\_ClientCertificate](_rcp___client_certificate.md) [Rcp\_ClientCertificate](remote-communication-overview.md#rcp_clientcertificate) | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| typedef enum [Rcp\_RemoteValidationType](remote-communication-overview.md#rcp_remotevalidationtype) [Rcp\_RemoteValidationType](remote-communication-overview.md#rcp_remotevalidationtype) | 远程验证类型。 |
| typedef struct [Rcp\_SecurityConfiguration](_rcp___security_configuration.md) [Rcp\_SecurityConfiguration](remote-communication-overview.md#rcp_securityconfiguration) | 请求的安全配置。 |
| typedef enum [Rcp\_ProxyTunnelMode](remote-communication-overview.md#rcp_proxytunnelmode) [Rcp\_ProxyTunnelMode](remote-communication-overview.md#rcp_proxytunnelmode) | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。 |
| typedef struct [Rcp\_WebProxy](_rcp___web_proxy.md) [Rcp\_WebProxy](remote-communication-overview.md#rcp_webproxy) | 自定义代理配置。 |
| typedef struct [Rcp\_IpAndPort](_rcp___ip_and_port.md) [Rcp\_IpAndPort](remote-communication-overview.md#rcp_ipandport) | 该接口用在[Rcp\_DnsServers](_rcp___dns_servers.md)中，表示一个DNS服务器的地址和端口。 |
| typedef struct [Rcp\_DnsServers](_rcp___dns_servers.md) [Rcp\_DnsServers](remote-communication-overview.md#rcp_dnsservers) | DNS服务器。[Rcp\_DnsConfiguration.dnsRules](_rcp___dns_configuration.md#dnsrules)中的类型之一。 |
| typedef struct [Rcp\_IpAddress](_rcp___ip_address.md) [Rcp\_IpAddress](remote-communication-overview.md#rcp_ipaddress) | 指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](_rcp___static_dns_rule_item.md)。 |
| typedef struct [Rcp\_StaticDnsRuleItem](_rcp___static_dns_rule_item.md) [Rcp\_StaticDnsRuleItem](remote-communication-overview.md#rcp_staticdnsruleitem) | 描述单个静态DNS规则。 |
| typedef struct [Rcp\_StaticDnsRule](_rcp___static_dns_rule.md) [Rcp\_StaticDnsRule](remote-communication-overview.md#rcp_staticdnsrule) | 静态DNS规则。 |
| typedef [Rcp\_IpAddress](_rcp___ip_address.md) \*(\* [Rcp\_DynamicDnsRuleFunction](remote-communication-overview.md#rcp_dynamicdnsrulefunction)) (const char \*host, uint16\_t port) | 一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。 |
| typedef enum [Rcp\_DnsRuleType](remote-communication-overview.md#rcp_dnsruletype) [Rcp\_DnsRuleType](remote-communication-overview.md#rcp_dnsruletype) | DNS规则类型。用于区分[Rcp\_DnsRule](_rcp___dns_rule.md)中使用的dns规则类型。 |
| typedef struct [Rcp\_DnsRule](_rcp___dns_rule.md) [Rcp\_DnsRule](remote-communication-overview.md#rcp_dnsrule) | DNS规则配置。 |
| typedef size\_t(\* [Rcp\_OnDataReceiveCallbackFunc](remote-communication-overview.md#rcp_ondatareceivecallbackfunc)) (void \*usrObject, const char \*data) | 接收到响应正文时调用的回调函数（字符数据）。 |
| typedef size\_t(\* [Rcp\_OnBinaryReceiveCallbackFunc](remote-communication-overview.md#rcp_onbinaryreceivecallbackfunc)) (void \*usrObject, [Rcp\_Buffer](_rcp___buffer.md) \*buffer) | 接收到响应正文时调用的回调函数（二进制数据）。 |
| typedef void (\* [Rcp\_OnStatusCodeReceiveCallbackFunc](remote-communication-overview.md#rcp_onstatuscodereceivecallbackfunc))(void \*usrObject, uint32\_t statusCode) | 接收到响应状态码时调用的回调函数。 |
| typedef void(\* [Rcp\_OnProgressCallbackFunc](remote-communication-overview.md#rcp_onprogresscallbackfunc)) (void \*usrObject, uint64\_t totalSize, uint64\_t transferredSize) | 请求/响应数据传输过程中调用的回调函数。 |
| typedef void(\* [Rcp\_OnHeaderReceiveCallbackFunc](remote-communication-overview.md#rcp_onheaderreceivecallbackfunc)) (void \*usrObject, [Rcp\_Headers](remote-communication-overview.md#rcp_headers) \*headers) | 收到所有请求时调用的回调。 |
| typedef void(\* [Rcp\_OnVoidCallbackFunc](remote-communication-overview.md#rcp_onvoidcallbackfunc)) (void \*usrObject) | 请求的DataEnd或Canceled事件回调的回调函数。 |
| typedef struct [Rcp\_OnDataReceiveCallback](_rcp___on_data_receive_callback.md) [Rcp\_OnDataReceiveCallback](remote-communication-overview.md#rcp_ondatareceivecallback) | 接收到数据时回调。[Rcp\_EventsHandler](_rcp___events_handler.md)中的配置。 |
| typedef struct [Rcp\_OnProgressCallback](_rcp___on_progress_callback.md) [Rcp\_OnProgressCallback](remote-communication-overview.md#rcp_onprogresscallback) | 收发时回调配置，在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置。 |
| typedef struct [Rcp\_OnHeaderReceiveCallback](_rcp___on_header_receive_callback.md) [Rcp\_OnHeaderReceiveCallback](remote-communication-overview.md#rcp_onheaderreceivecallback) | [Rcp\_EventsHandler](_rcp___events_handler.md)中配置的接收到的header回调配置。 |
| typedef struct [Rcp\_OnVoidCallback](_rcp___on_void_callback.md) [Rcp\_OnVoidCallback](remote-communication-overview.md#rcp_onvoidcallback) | 在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置的数据结束或已取消事件的回调配置。 |
| typedef struct [Rcp\_EventsHandler](_rcp___events_handler.md) [Rcp\_EventsHandler](remote-communication-overview.md#rcp_eventshandler) | 监听不同HTTP事件的回调函数。 |
| typedef struct [Rcp\_Timeout](_rcp___timeout.md) [Rcp\_Timeout](remote-communication-overview.md#rcp_timeout) | 请求的超时配置。 |
| typedef struct [Rcp\_DnsOverHttps](_rcp___dns_over_https.md) [Rcp\_DnsOverHttps](remote-communication-overview.md#rcp_dnsoverhttps) | HTTPS上的DNS配置如果设置，则首选由DOH DNS服务器解析的地址。 |
| typedef enum [Rcp\_PathPreference](remote-communication-overview.md#rcp_pathpreference) [Rcp\_PathPreference](remote-communication-overview.md#rcp_pathpreference) | 请求路径首选项。 |
| typedef struct [Rcp\_TransferConfiguration](_rcp___transfer_configuration.md) [Rcp\_TransferConfiguration](remote-communication-overview.md#rcp_transferconfiguration) | 传输配置。 |
| typedef struct [Rcp\_InfoToCollect](_rcp___info_to_collect.md) [Rcp\_InfoToCollect](remote-communication-overview.md#rcp_infotocollect) | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| typedef struct [Rcp\_TracingConfiguration](_rcp___tracing_configuration.md) [Rcp\_TracingConfiguration](remote-communication-overview.md#rcp_tracingconfiguration) | 请求追踪配置。 |
| typedef enum [Rcp\_ProxyType](remote-communication-overview.md#rcp_proxytype) [Rcp\_ProxyType](remote-communication-overview.md#rcp_proxytype) | 代理类型。用于区分不同的代理配置。 |
| typedef struct [Rcp\_ProxyConfiguration](_rcp___proxy_configuration.md) [Rcp\_ProxyConfiguration](remote-communication-overview.md#rcp_proxyconfiguration) | 代理配置。 |
| typedef struct [Rcp\_DnsConfiguration](_rcp___dns_configuration.md) [Rcp\_DnsConfiguration](remote-communication-overview.md#rcp_dnsconfiguration) | DNS解析配置。 |
| typedef struct [Rcp\_Configuration](_rcp___configuration.md) [Rcp\_Configuration](remote-communication-overview.md#rcp_configuration) | 请求配置。 |
| typedef struct [Rcp\_TransferRange](_rcp___transfer_range.md) [Rcp\_TransferRange](remote-communication-overview.md#rcp_transferrange) | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅返回HTTP响应的一部分。 |
| typedef struct [Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies) [Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies) | 请求Cookie。 |
| typedef struct [Rcp\_Request](_rcp___request.md) [Rcp\_Request](remote-communication-overview.md#rcp_request) | 网络请求。 |
| typedef struct [Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md) [Rcp\_RequestCookieEntry](remote-communication-overview.md#rcp_requestcookieentry) | 描述请求的所有Cookie键值对。 |
| typedef enum [Rcp\_StatusCode](remote-communication-overview.md#rcp_statuscode) [Rcp\_StatusCode](remote-communication-overview.md#rcp_statuscode) | 请求响应的状态码。 |
| typedef enum [Rcp\_DebugEvent](remote-communication-overview.md#rcp_debugevent) [Rcp\_DebugEvent](remote-communication-overview.md#rcp_debugevent) | 描述调试信息的事件类型。 |
| typedef struct [Rcp\_DebugInfo](_rcp___debug_info.md) [Rcp\_DebugInfo](remote-communication-overview.md#rcp_debuginfo) | 描述存储在[Rcp\_Response](_rcp___response.md)中的调试信息的结构。 |
| typedef struct [Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes) [Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes) | 描述[Rcp\_Response](_rcp___response.md)中Cookie属性的类型。 |
| typedef struct [Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md) [Rcp\_CookieAttributeEntry](remote-communication-overview.md#rcp_cookieattributeentry) | 响应Cookie属性条目。 |
| typedef struct [Rcp\_ResponseCookies](_rcp___response_cookies.md) [Rcp\_ResponseCookies](remote-communication-overview.md#rcp_responsecookies) | 响应Cookie。 |
| typedef struct [Rcp\_TimeInfo](_rcp___time_info.md) [Rcp\_TimeInfo](remote-communication-overview.md#rcp_timeinfo) | 响应计时信息。 |
| typedef struct [Rcp\_Response](_rcp___response.md) [Rcp\_Response](remote-communication-overview.md#rcp_response) | 网络请求的响应。 |
| typedef void(\* [Rcp\_ResponseCallback](remote-communication-overview.md#rcp_responsecallback)) (void \*usrCtx, [Rcp\_Response](_rcp___response.md) \*response, uint32\_t errCode) | 响应回调函数指针。 |
| typedef struct [Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md) [Rcp\_ResponseCallbackObject](remote-communication-overview.md#rcp_responsecallbackobject) | 响应回调结构体。 |
| typedef struct [Rcp\_RequestHandler](remote-communication-overview.md#rcp_requesthandler) [Rcp\_RequestHandler](remote-communication-overview.md#rcp_requesthandler) | 与[Rcp\_Interceptor](_rcp___interceptor.md)关联的异步处理器。 |
| typedef struct [Rcp\_SyncRequestHandler](remote-communication-overview.md#rcp_syncrequesthandler) [Rcp\_SyncRequestHandler](remote-communication-overview.md#rcp_syncrequesthandler) | 与[Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)关联的同步处理器。 |
| typedef struct [Rcp\_Interceptor](_rcp___interceptor.md) [Rcp\_Interceptor](remote-communication-overview.md#rcp_interceptor) | 异步拦截器。 |
| typedef struct [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md) [Rcp\_SyncInterceptor](remote-communication-overview.md#rcp_syncinterceptor) | 同步拦截器。 |
| typedef struct [Rcp\_InterceptorArray](_rcp___interceptor_array.md) [Rcp\_InterceptorArray](remote-communication-overview.md#rcp_interceptorarray) | 异步拦截器数组。 |
| typedef struct [Rcp\_SyncInterceptorArray](_rcp___sync_interceptor_array.md) [Rcp\_SyncInterceptorArray](remote-communication-overview.md#rcp_syncinterceptorarray) | 同步拦截器数组。 |
| typedef enum [Rcp\_SessionType](remote-communication-overview.md#rcp_sessiontype) [Rcp\_SessionType](remote-communication-overview.md#rcp_sessiontype) | 会话类型。 |
| typedef struct [Rcp\_Session](remote-communication-overview.md#rcp_session) [Rcp\_Session](remote-communication-overview.md#rcp_session) | 会话。 |
| typedef struct [Rcp\_SessionListener](_rcp___session_listener.md) [Rcp\_SessionListener](remote-communication-overview.md#rcp_sessionlistener) | 关闭或取消会话事件的回调函数。 |
| typedef struct [Rcp\_ConnectionConfiguration](_rcp___connection_configuration.md) [Rcp\_ConnectionConfiguration](remote-communication-overview.md#rcp_connectionconfiguration) | 连接配置。 |
| typedef struct [Rcp\_SessionConfiguration](_rcp___session_configuration.md) [Rcp\_SessionConfiguration](remote-communication-overview.md#rcp_sessionconfiguration) | 会话配置。 |
| typedef struct [Rcp\_OnBinaryReceiveCallback](_rcp___on_binary_receive_callback.md) [Rcp\_OnBinaryReceiveCallback](remote-communication-overview.md#rcp_onbinaryreceivecallback) | 接收到响应的二进制数据时的回调。 |
| typedef struct [Rcp\_OnStatusCodeReceiveCallback](_rcp___on_status_code_callback.md) [Rcp\_OnStatusCodeReceiveCallback](remote-communication-overview.md#rcp_onstatuscodereceivecallback) | 接收到响应的状态码时的回调。 |
| typedef struct [Rcp\_OnGetDataCallback](_rcp___on_get_data_callback.md)  [Rcp\_OnGetDataCallback](remote-communication-overview.md#rcp_ongetdatacallback) | 获取数据的回调。 |
| typedef size\_t(\* [Rcp\_GetDataCallbackFunc](remote-communication-overview.md#rcp_getdatacallbackfunc)) (void \*userObject, uint8\_t \*outData, size\_t size) | 获取数据的回调函数。 |
| typedef void [Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) | quic连接实例的类型。 |
| typedef void [Rcp\_QuicSession](remote-communication-overview.md#rcp_quicsession) | quic会话的类型，可以管理多个连接实例。 |
| typedef struct [Rcp\_QuicSlist](_rcp___quic_slist.md) [Rcp\_QuicSlist](remote-communication-overview.md#rcp_quicslist) | 链表数据结构。 |
| typedef enum [RCP\_QuicIpResolve](remote-communication-overview.md#rcp_quicipresolve) [RCP\_QuicIpResolve](remote-communication-overview.md#rcp_quicipresolve) | 请求DNS解析时使用的IP解析类型。 |
| typedef struct [Rcp\_QuicIpAddress](_rcp___quic_ipaddress.md) [Rcp\_QuicIpAddress](remote-communication-overview.md#rcp_quicipaddress) | 用于存储IP地址的数据结构。 |
| typedef [Rcp\_QuicIpAddress](_rcp___quic_ipaddress.md) (\*[Rcp\_QuicDynamicDnsRuleFunction](remote-communication-overview.md#rcp_quicdynamicdnsrulefunction)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, const char \*host, uint16\_t port) | 自定义DNS解析回调函数，根据主机名和端口返回IP地址。 |
| typedef enum [Rcp\_QuicConnOpt](remote-communication-overview.md#rcp_quicconnopt) | quic连接选项类型，用于配置连接的各种参数和回调函数。 |
| typedef enum [Rcp\_QuicStreamOpt](remote-communication-overview.md#rcp_quicstreamopt) | quic流选项类型，用于配置流的各种参数和回调函数。 |
| typedef enum [Rcp\_QuicConnInfo](remote-communication-overview.md#rcp_quicconninfo) | quic连接信息类型。用于查询连接的各种信息。 |
| typedef enum [Rcp\_QuicStreamInfo](remote-communication-overview.md#rcp_quicstreaminfo) | quic流信息类型。用于查询流的各种信息。 |
| typedef enum [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) | quic请求中可能出现的错误码。 |
| typedef enum [Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection) | quic流的方向类型。 |
| typedef enum [Rcp\_QuicStreamShutdown](remote-communication-overview.md#rcp_quicstreamshutdown) | quic流的关闭操作的类型。用于指定关闭流的读或写方向。 |
| typedef struct [Rcp\_QuicIoVec](_rcp___quic_io_vec.md) [Rcp\_QuicIoVec](remote-communication-overview.md#rcp_quiciovec) | 用于存储二进制内容的数据结构。 |
| typedef struct [Rcp\_QuicStreamData](_rcp___quic_stream_data.md) [Rcp\_QuicStreamData](remote-communication-overview.md#rcp_quicstreamdata) | quic连接中用于接收流式数据的存储结构。 |
| typedef [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) (\*[Rcp\_QuicConnectionOnCertAuthority](remote-communication-overview.md#rcp_quicconnectiononcertauthority)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, const unsigned char \*const \*certs, const size\_t \*certLens, size\_t certsCount) | 证书校验的回调函数。在quic建链时，用于自定义校验对端证书。 |
| typedef void (\*[Rcp\_QuicConnectionOnSessionTicketUpdate](remote-communication-overview.md#rcp_quicconnectiononsessionticketupdate)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, const char \*sessionTicket, size\_t length) | quic会话票据更新回调函数。在quic会话中票据更新时触发，返回新的票据。 |
| typedef void (\*[Rcp\_QuicConnectionOnConnected](remote-communication-overview.md#rcp_quicconnectiononconnected)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject) | quic连接成功回调函数。quic连接成功建立时触发该函数。 |
| typedef void (\*[Rcp\_QuicConnectionOnError](remote-communication-overview.md#rcp_quicconnectiononerror)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) errCode, const char \*errDetail) | quic连接失败回调函数。quic连接建立失败时触发该函数，返回失败原因。 |
| typedef void (\*[Rcp\_QuicConnectionOnClosed](remote-communication-overview.md#rcp_quicconnectiononclosed)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject) | quic连接关闭回调函数。quic连接关闭时触发，通知连接已关闭。 |
| typedef void (\*[Rcp\_QuicConnectionOnStreamInbound](remote-communication-overview.md#rcp_quicconnectiononstreaminbound)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, uint64\_t streamId) | quic连接中入站流回调函数。当quic连接中对端创建流时触发，处理对端发起的流，设置流的选项和回调。 |
| typedef void (\*[Rcp\_QuicStreamOnEvent](remote-communication-overview.md#rcp_quicstreamonevent)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, uint64\_t streamId, [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) errCode, const char \*errDetail) | quic连接中流事件回调函数。当quic连接中的流发生事件时触发，用于处理流的状态变化和错误。 |
| typedef uint64\_t (\*[Rcp\_QuicStreamOnReceiveData](remote-communication-overview.md#rcp_quicstreamonreceivedata)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, uint64\_t streamId, const [Rcp\_QuicStreamData](remote-communication-overview.md#rcp_quicstreamdata) \*streamData) | quic连接中流数据接收回调函数。当quic连接中接收到流数据时触发，用于处理接收到的数据。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [Rcp\_FormValueType](remote-communication-overview.md#rcp_formvaluetype) {  RCP\_FORM\_VALUE\_TYPE\_INT32, RCP\_FORM\_VALUE\_TYPE\_INT64, RCP\_FORM\_VALUE\_TYPE\_BOOL, RCP\_FORM\_VALUE\_TYPE\_STRING,  RCP\_FORM\_VALUE\_TYPE\_DOUBLE  } | 表单值类型。 |
| [Rcp\_ContentOrPathOrCallbackType](remote-communication-overview.md#rcp_contentorpathorcallbacktype) { RCP\_FILE\_VALUE\_TYPE\_CONTENT, RCP\_FILE\_VALUE\_TYPE\_PATH, RCP\_FILE\_VALUE\_TYPE\_CALLBACK } | 回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md)中使用的数据。 |
| [Rcp\_MultipartValueType](remote-communication-overview.md#rcp_multipartvaluetype) { RCP\_TYPE\_FORM\_FIELD\_VALUE, RCP\_TYPE\_FORM\_FIELD\_FILE\_VALUE } | 多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)中使用的数据。 |
| [Rcp\_ContentType](remote-communication-overview.md#rcp_contenttype) { RCP\_CONTENT\_TYPE\_STRING, RCP\_CONTENT\_TYPE\_FORM, RCP\_CONTENT\_TYPE\_MULTIPARTFORM, RCP\_CONTENT\_TYPE\_GETCALLBACK } | 内容类型。用于区分[Rcp\_RequestContent](_rcp___request_content.md)中使用的数据。 |
| [Rcp\_AuthenticationType](remote-communication-overview.md#rcp_authenticationtype) { RCP\_AUTHENTICATION\_AUTO, RCP\_AUTHENTICATION\_BASIC, RCP\_AUTHENTICATION\_NTLM, RCP\_AUTHENTICATION\_DIGEST } | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| [Rcp\_ExclusionsValueType](remote-communication-overview.md#rcp_exclusionsvaluetype) { RCP\_EXCLUSION\_USE\_URL\_ARRAY, RCP\_EXCLUSION\_USE\_CALLBACK } | 代理排除中使用的数据类型，用于区分[Rcp\_Exclusions](_rcp___exclusions.md)中使用的数据。 |
| [Rcp\_CertType](remote-communication-overview.md#rcp_certtype) { RCP\_CERT\_PEM, RCP\_CERT\_DER, RCP\_CERT\_P12 } | 客户端证书类型。 |
| [Rcp\_RemoteValidationType](remote-communication-overview.md#rcp_remotevalidationtype) { RCP\_REMOTE\_VALIDATION\_SYSTEM, RCP\_REMOTE\_VALIDATION\_SKIP, RCP\_REMOTE\_VALIDATION\_CERTIFICATE\_AUTHORITY } | 远程验证类型。 |
| [Rcp\_ProxyTunnelMode](remote-communication-overview.md#rcp_proxytunnelmode) { RCP\_PROXY\_TUNNEL\_AUTO, RCP\_PROXY\_TUNNEL\_ALWAYS } | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。 |
| [Rcp\_DnsRuleType](remote-communication-overview.md#rcp_dnsruletype) { RCP\_DNS\_RULE\_DNS\_SERVERS, RCP\_DNS\_RULE\_STATIC, RCP\_DNS\_RULE\_DYNAMIC } | DNS规则类型。用于区分[Rcp\_DnsRule](_rcp___dns_rule.md)中使用的DNS规则类型。 |
| [Rcp\_PathPreference](remote-communication-overview.md#rcp_pathpreference) { RCP\_PATH\_PREFERENCE\_AUTO, RCP\_PATH\_PREFERENCE\_WIFI, RCP\_PATH\_PREFERENCE\_CELLULAR } | 请求路径首选项。 |
| [Rcp\_ProxyType](remote-communication-overview.md#rcp_proxytype) { RCP\_PROXY\_SYSTEM, RCP\_PROXY\_CUSTOM, RCP\_PROXY\_NO\_PROXY } | 代理类型。用于区分不同的代理配置。 |
| [Rcp\_StatusCode](remote-communication-overview.md#rcp_statuscode) {  RCP\_NONE = 0, RCP\_OK = 200, RCP\_CREATED, RCP\_ACCEPTED,  RCP\_NOT\_AUTHORITATIVE, RCP\_NO\_CONTENT, RCP\_RESET, RCP\_PARTIAL,  RCP\_MULTI\_CHOICE = 300, RCP\_MOVED\_PERMANENTLY, RCP\_MOVED\_TEMPORARILY, RCP\_SEE\_OTHER,  RCP\_NOT\_MODIFIED, RCP\_USE\_PROXY, RCP\_BAD\_REQUEST = 400, RCP\_UNAUTHORIZED,  RCP\_PAYMENT\_REQUIRED, RCP\_FORBIDDEN, RCP\_NOT\_FOUND, RCP\_BAD\_METHOD,  RCP\_NOT\_ACCEPTABLE, RCP\_PROXY\_AUTH, RCP\_CLIENT\_TIMEOUT, RCP\_CONFLICT,  RCP\_GONE, RCP\_LENGTH\_REQUIRED, RCP\_PRECON\_FAILED, RCP\_ENTITY\_TOO\_LARGE,  RCP\_REQ\_TOO\_LONG, RCP\_UNSUPPORTED\_TYPE, RCP\_INTERNAL\_ERROR = 500, RCP\_NOT\_IMPLEMENTED,  RCP\_BAD\_GATEWAY, RCP\_UNAVAILABLE, RCP\_GATEWAY\_TIMEOUT, RCP\_VERSION  } | 请求响应的状态码。 |
| [Rcp\_DebugEvent](remote-communication-overview.md#rcp_debugevent) {  RCP\_DEBUG\_EVENT\_TEXT, RCP\_DEBUG\_EVENT\_HEADER\_IN, RCP\_DEBUG\_EVENT\_HEADER\_OUT, RCP\_DEBUG\_EVENT\_DATA\_IN,  RCP\_DEBUG\_EVENT\_DATA\_OUT, RCP\_DEBUG\_EVENT\_SSL\_DATA\_IN, RCP\_DEBUG\_EVENT\_SSL\_DATA\_OUT  } | 描述调试信息的事件类型。 |
| [Rcp\_SessionType](remote-communication-overview.md#rcp_sessiontype) { RCP\_SESSION\_TYPE\_HTTP = 0, RCP\_SESSION\_TYPE\_MAX = 100 } | 会话类型。 |
| [RCP\_QuicIpResolve](remote-communication-overview.md#rcp_quicipresolve) {RCP\_QUIC\_IP\_RESOLVE\_WHATEVER = 0, RCP\_QUIC\_IP\_RESOLVE\_V4, RCP\_QUIC\_IP\_RESOLVE\_V6} | 请求DNS解析时使用的IP解析类型。 |
| [Rcp\_QuicConnOpt](remote-communication-overview.md#rcp_quicconnopt) { RCP\_QUIC\_CONN\_IP\_ADDRESS = 0, RCP\_QUIC\_CONN\_IP\_RESOLVE, RCP\_QUIC\_CONN\_DNS\_FUNCTION, RCP\_QUIC\_CONN\_ON\_CONNECTED\_FUNCTION, RCP\_QUIC\_CONN\_ON\_ERROR\_FUNCTION, RCP\_QUIC\_CONN\_ON\_CLOSED\_FUNCTION, RCP\_QUIC\_CONN\_STREAM\_INBOUND\_FUNCTION, RCP\_QUIC\_CONN\_CONNECT\_TIMEOUT\_MS, RCP\_QUIC\_CONN\_IDLE\_TIMEOUT\_MS, RCP\_QUIC\_TLS\_CERT\_AUTHORITY\_FUNCTION = 1000, RCP\_QUIC\_TLS\_CERT\_AUTHORITY\_CONTENT, RCP\_QUIC\_TLS\_SESSION\_TICKET\_UPDATE\_FUNCTION, RCP\_QUIC\_TLS\_SESSION\_TICKET\_CONTENT, RCP\_QUIC\_TP\_INITIAL\_MAX\_BIDIRECTIONAL\_STREAMS = 2000, RCP\_QUIC\_TP\_INITIAL\_MAX\_DATA, RCP\_QUIC\_TP\_INITIAL\_MAX\_STREAMDATA\_BIDIRECTIONAL\_LOCAL, RCP\_QUIC\_TP\_INITIAL\_MAX\_STREAMDATA\_BIDIRECTIONAL\_REMOTE, RCP\_QUIC\_TP\_INITIAL\_MAX\_STREAMDATA\_UNIDIRECTIONAL, RCP\_QUIC\_TP\_INITIAL\_MAX\_UNIDIRECTIONAL\_STREAMS} | quic连接选项类型。 |
| [Rcp\_QuicStreamOpt](remote-communication-overview.md#rcp_quicstreamopt) { RCP\_QUIC\_STREAM\_EVENT\_FUNCTION = 0, RCP\_QUIC\_STREAM\_DATA\_FUNCTION, RCP\_QUIC\_INBOUND\_STREAM\_USER\_OBJECT, RCP\_QUIC\_STREAM\_SND\_BUFFER\_SIZE\_KB} | quic连接中配置流选项。 |
| [Rcp\_QuicConnInfo](remote-communication-overview.md#rcp_quicconninfo) { RCP\_INFO\_CONN\_GET\_LOCALADDR = 0, RCP\_INFO\_CONN\_GET\_PEERADDR, RCP\_INFO\_CONN\_DNS\_TIME\_MS, RCP\_INFO\_CONN\_CONNECT\_TIME\_MS, RCP\_INFO\_CONN\_SCID, RCP\_INFO\_CONN\_DCID } | quic连接中的信息类型。 |
| [Rcp\_QuicStreamInfo](remote-communication-overview.md#rcp_quicstreamopt) { RCP\_INFO\_STREAM\_SND\_BUFFER\_SIZE\_KB = 0 } | quic流中的信息类型。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) { RCP\_QUIC\_ERROR\_CODE\_SUCCESS, RCP\_QUIC\_PERMISSION\_DENIED, RCP\_QUIC\_ERROR\_CODE\_FAILED, RCP\_QUIC\_ERROR\_CODE\_INVALID\_PARAM, RCP\_QUIC\_ERROR\_CODE\_INVALID\_STATE, RCP\_QUIC\_ERROR\_CODE\_OUT\_OF\_MEM, RCP\_QUIC\_ERROR\_CODE\_CLOSE\_FROM\_PEER, RCP\_QUIC\_ERROR\_CODE\_HANDSHAKE\_TIMEOUT, RCP\_QUIC\_ERROR\_CODE\_NETWORK\_IDLE\_TIMEOUT, RCP\_QUIC\_ERROR\_INVALID\_FRAME, RCP\_QUIC\_ERROR\_CODE\_SEND\_PENDING, RCP\_QUIC\_ERROR\_CODE\_FINALIZE\_PENDING, RCP\_QUIC\_ERROR\_CODE\_NETWORK\_UNREACHABLE, RCP\_QUIC\_ERROR\_CODE\_ENCRYPT\_ERROR, RCP\_QUIC\_ERROR\_CODE\_BUFFER\_TOO\_SMALL, RCP\_QUIC\_ERROR\_CODE\_EAGAIN, RCP\_QUIC\_ERROR\_CODE\_STREAM\_CLOSED, RCP\_QUIC\_ERROR\_CODE\_STREAM\_RESET\_RECEIVED, RCP\_QUIC\_ERROR\_CODE\_STREAM\_STOP\_SENDING\_RECEIVED } | quic请求中可能出现的错误码。 |
| [Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection) { RCP\_QUIC\_STREAM\_BIDI = 0, RCP\_QUIC\_STREAM\_UNI } | quic流的方向类型。 |
| [Rcp\_QuicStreamShutdown](remote-communication-overview.md#rcp_quicstreamshutdown) { RCP\_QUIC\_STREAM\_SHUTDOWN\_READ = 1, RCP\_QUIC\_STREAM\_SHUTDOWN\_WRITE = 2 } | quic流的关闭操作的类型。用于指定关闭流的读或写方向。 |

### 函数

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
| uint32\_t [HMS\_Rcp\_SetFormOrder](remote-communication-overview.md#hms_rcp_setformorder) ([Rcp\_Form](remote-communication-overview.md#rcp_form) \*form, [Rcp\_FormOrder](remote-communication-overview.md#rcp_formorder) order) | 设置Form表单的键值对发送顺序。 |
| uint32\_t [HMS\_Rcp\_SetMultipartFormOrder](remote-communication-overview.md#hms_rcp_setmultipartformorder) ([Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform) \*multipartForm, [Rcp\_FormOrder](remote-communication-overview.md#rcp_formorder) order) | 设置MultipartForm表单的键值对发送顺序。 |
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
| uint32\_t [HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](remote-communication-overview.md#hms_rcp_setrequestonbinarydatarecvcallback) ([Rcp\_Request](remote-communication-overview.md#rcp_request) \*request, [Rcp\_OnBinaryReceiveCallback](remote-communication-overview.md#rcp_onbinaryreceivecallback) onBinaryReceiveCallback) | 为请求设置流式接收二进制数据的回调函数。该回调函数与[Rcp\_Configuration](_rcp___configuration.md)中配置的[Rcp\_OnDataReceiveCallback](remote-communication-overview.md#rcp_ondatareceivecallback)功能一致。设置后将替换在[Rcp\_Configuration](_rcp___configuration.md)中配置的[Rcp\_OnDataReceiveCallback](remote-communication-overview.md#rcp_ondatareceivecallback)。 |
| uint32\_t [HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback](remote-communication-overview.md#hms_rcp_setrequestonstatuscodereceivecallback) ([Rcp\_Request](remote-communication-overview.md#rcp_request) \*request, [Rcp\_OnStatusCodeReceiveCallback](remote-communication-overview.md#rcp_onstatuscodereceivecallback) onStatusCodeReceiveCallback) | 为请求设置响应状态码接收回调函数。 |
| uint32\_t [HMS\_Rcp\_GetDefaultSession](remote-communication-overview.md#hms_rcp_getdefaultsession) ([Rcp\_Session](remote-communication-overview.md#rcp_session) \*\*session) | 获取默认会话。 |
| uint32\_t [HMS\_Rcp\_SetRequestConnectOnly](remote-communication-overview.md#hms_rcp_setrequestconnectonly) ([Rcp\_Request](remote-communication-overview.md#rcp_request) \*request, bool connectOnly) | 设置请求仅用于建立连接，而不进行数据传输。 |
| uint32\_t [HMS\_Rcp\_SetRequestGetDataCallback](remote-communication-overview.md#hms_rcp_setrequestgetdatacallback) ([Rcp\_Request](_rcp___request.md) \*request, [Rcp\_OnGetDataCallback](_rcp___on_get_data_callback.md)  getDataCallback) | 设置获取数据的回调函数。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnSetOpt](remote-communication-overview.md#hms_rcp_quicconnsetopt) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, [Rcp\_QuicConnOpt](remote-communication-overview.md#rcp_quicconnopt) opt, const void \*optVal, uint32\_t optLen) | 设置quic连接选项。用于设置连接的各种参数和回调函数。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnGetInfo](remote-communication-overview.md#hms_rcp_quicconngetinfo) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, [Rcp\_QuicConnInfo](remote-communication-overview.md#rcp_quicconninfo) info, void \*infoVal, uint32\_t \*infoLen) | 获取quic连接信息。用于建立quic连接成功后，获取相关quic连接信息。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicStreamSetOpt](remote-communication-overview.md#hms_rcp_quicstreamsetopt) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, [Rcp\_QuicStreamOpt](remote-communication-overview.md#rcp_quicstreamopt) opt, const void \*optVal, uint32\_t optLen) | 设置quic连接中流的参数。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicStreamGetInfo](remote-communication-overview.md#hms_rcp_quicstreamgetinfo) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, [Rcp\_QuicStreamInfo](remote-communication-overview.md#rcp_quicstreaminfo) info, void \*infoVal, uint32\_t \*infoLen) | 获取quic连接中streamId对应流的信息。 |
| [Rcp\_QuicSession](remote-communication-overview.md#rcp_quicsession) \* [HMS\_Rcp\_QuicCreateSession](remote-communication-overview.md#hms_rcp_quiccreatesession) () | 创建quic会话对象。一个quic会话中可以管理多个quic连接。 |
| void [HMS\_Rcp\_QuicDestroySession](remote-communication-overview.md#hms_rcp_quicdestroysession) ([Rcp\_QuicSession](remote-communication-overview.md#rcp_quicsession) \*session) | 销毁quic会话对象。释放quic会话资源。 |
| [Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \* [HMS\_Rcp\_QuicConnCreate](remote-communication-overview.md#hms_rcp_quicconncreate) (char \*alpn, void \*userObject) | 创建quic连接对象。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnConnect](remote-communication-overview.md#hms_rcp_quicconnconnect) ([Rcp\_QuicSession](remote-communication-overview.md#rcp_quicsession) \*session, [Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, const char \*serverName, uint16\_t port) | 发起quic连接握手。握手结果通过连接回调通知。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnDestroy](remote-communication-overview.md#hms_rcp_quicconndestroy) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn) | 销毁quic连接对象。释放quic连接资源。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamOpen](remote-communication-overview.md#hms_rcp_quicconnstreamopen) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, [Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection) direction, uint64\_t \*streamId, void \*userObject) | 在quic连接中打开一个quic流。quic连接建立成功后才能打开quic流。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamSend](remote-communication-overview.md#hms_rcp_quicconnstreamsend) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, const [Rcp\_QuicIoVec](_rcp___quic_io_vec.md) \*ioVec, uint32\_t ioVecCount, bool fin) | 通过quic流发送数据。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamWantRead](remote-communication-overview.md#hms_rcp_quicconnstreamwantread) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId) | 触发quic流数据读取回调。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamReset](remote-communication-overview.md#hms_rcp_quicconnstreamreset) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, uint64\_t appErr) | 重置quic流。立即终止流，丢弃所有未发送和已接收的数据。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamShutdown](remote-communication-overview.md#hms_rcp_quicconnstreamshutdown) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, [Rcp\_QuicStreamShutdown](remote-communication-overview.md#rcp_quicstreamshutdown) flag, uint64\_t appErr) | 关闭连接中streamId对应流的读或写。 |
| [Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection) [HMS\_Rcp\_QuicStreamGetDirection](remote-communication-overview.md#hms_rcp_quicstreamgetdirection) (uint64\_t streamId) | 获取quic流的方向类型。 |
| void [HMS\_Rcp\_QuicFreeSlist](remote-communication-overview.md#hms_rcp_quicfreeslist) ([Rcp\_QuicSlist](_rcp___quic_slist.md) \*list) | 释放[Rcp\_QuicSlist](_rcp___quic_slist.md)链表，释放链表中的所有节点和数据。 |

## 宏定义说明

### RCP\_HOST\_MAX\_LEN

```cpp
#define RCP_HOST_MAX_LEN   256
```

**描述**

主机名的最大长度。

**起始版本：** 5.0.0(12)

### RCP\_IP\_MAX\_LEN

```cpp
#define RCP_IP_MAX_LEN   40
```

**描述**

IP地址的最大长度。

**起始版本：** 5.0.0(12)

### RCP\_MAX\_CONTENT\_TYPE\_LEN

```cpp
#define RCP_MAX_CONTENT_TYPE_LEN   64
```

**描述**

内容类型最大长度。

**起始版本：** 5.0.0(12)

### RCP\_MAX\_FILENAME\_LEN

```cpp
#define RCP_MAX_FILENAME_LEN   128
```

**描述**

文件名最大长度。

**起始版本：** 5.0.0(12)

### RCP\_MAX\_PATH\_LEN

```cpp
#define RCP_MAX_PATH_LEN   128
```

**描述**

路径的最大长度。

**起始版本：** 5.0.0(12)

### RCP\_MAX\_REQUEST\_ID\_LEN

```cpp
#define RCP_MAX_REQUEST_ID_LEN   32
```

**描述**

请求ID的最大长度。

**起始版本：** 5.0.0(12)

### RCP\_METHOD\_DELETE

```cpp
#define RCP_METHOD_DELETE   "DELETE"
```

**描述**

HTTP delete方法。

**起始版本：** 5.0.0(12)

### RCP\_METHOD\_GET

```cpp
#define RCP_METHOD_GET   "GET"
```

**描述**

HTTP get方法。

**起始版本：** 5.0.0(12)

### RCP\_METHOD\_HEAD

```cpp
#define RCP_METHOD_HEAD   "HEAD"
```

**描述**

HTTP head方法。

**起始版本：** 5.0.0(12)

### RCP\_METHOD\_OPTIONS

```cpp
#define RCP_METHOD_OPTIONS   "OPTIONS"
```

**描述**

HTTP options方法。

**起始版本：** 5.0.0(12)

### RCP\_METHOD\_PATCH

```cpp
#define RCP_METHOD_PATCH   "PATCH"
```

**描述**

HTTP patch方法。

**起始版本：** 5.0.0(12)

### RCP\_METHOD\_POST

```cpp
#define RCP_METHOD_POST   "POST"
```

**描述**

HTTP post方法。

**起始版本：** 5.0.0(12)

### RCP\_METHOD\_PUT

```cpp
#define RCP_METHOD_PUT   "PUT"
```

**描述**

HTTP put方法。

**起始版本：** 5.0.0(12)

### RCP\_METHOD\_TRACE

```cpp
#define RCP_METHOD_TRACE   "TRACE"
```

**描述**

HTTP trace方法。

**起始版本：** 5.0.0(12)

### RCP\_QUIC\_IP\_MAX\_LEN

```cpp
#define RCP_QUIC_IP_MAX_LEN   40
```

**描述**

quic连接的IP地址的最大长度。

**起始版本：** 26.0.0

## 类型定义说明

### Rcp\_AuthenticationType

```cpp
typedef enum Rcp_AuthenticationType Rcp_AuthenticationType
```

**描述**

枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。

**起始版本：** 5.0.0(12)

### Rcp\_Buffer

```cpp
typedef struct Rcp_Buffer Rcp_Buffer
```

**描述**

文本存储结构。

**起始版本：** 5.0.0(12)

### Rcp\_CertificateAuthority

```cpp
typedef struct Rcp_CertificateAuthority Rcp_CertificateAuthority
```

**描述**

用于验证远程服务器标识的证书颁发机构（CA）。

**起始版本：** 5.0.0(12)

### Rcp\_CertType

```cpp
typedef enum Rcp_CertType Rcp_CertType
```

**描述**

客户端证书类型。

**起始版本：** 5.0.0(12)

### Rcp\_ClientCertificate

```cpp
typedef struct Rcp_ClientCertificate Rcp_ClientCertificate
```

**描述**

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

**起始版本：** 5.0.0(12)

### Rcp\_Configuration

```cpp
typedef struct Rcp_Configuration Rcp_Configuration
```

**描述**

请求配置。

**起始版本：** 5.0.0(12)

### Rcp\_ConnectionConfiguration

```cpp
typedef struct Rcp_ConnectionConfiguration Rcp_ConnectionConfiguration
```

**描述**

连接配置。

**起始版本：** 5.0.0(12)

### Rcp\_ContentOrPathOrCallback

```cpp
typedef struct Rcp_ContentOrPathOrCallback Rcp_ContentOrPathOrCallback
```

**描述**

[Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md)中使用的简单表单数据字段值。

**起始版本：** 5.0.0(12)

### Rcp\_ContentOrPathOrCallbackType

```cpp
typedef enum Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallbackType
```

**描述**

回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md)中使用的数据。

**起始版本：** 5.0.0(12)

### Rcp\_ContentType

```cpp
typedef enum Rcp_ContentType Rcp_ContentType
```

**描述**

内容类型。用于区分[Rcp\_RequestContent](_rcp___request_content.md)中使用的数据。

**起始版本：** 5.0.0(12)

### Rcp\_CookieAttributeEntry

```cpp
typedef struct Rcp_CookieAttributeEntry Rcp_CookieAttributeEntry
```

**描述**

响应Cookie属性条目。

**起始版本：** 5.0.0(12)

### Rcp\_CookieAttributes

```cpp
typedef struct Rcp_CookieAttributes Rcp_CookieAttributes
```

**描述**

描述[Rcp\_Response](_rcp___response.md)中Cookie属性的类型。

**起始版本：** 5.0.0(12)

### Rcp\_Credential

```cpp
typedef struct Rcp_Credential Rcp_Credential
```

**描述**

服务器身份验证中使用的身份验证凭据，包括用户名和密码。

**起始版本：** 5.0.0(12)

### Rcp\_DebugEvent

```cpp
typedef enum Rcp_DebugEvent Rcp_DebugEvent
```

**描述**

描述调试信息的事件类型。

**起始版本：** 5.0.0(12)

### Rcp\_DebugInfo

```cpp
typedef struct Rcp_DebugInfo Rcp_DebugInfo
```

**描述**

描述存储在[Rcp\_Response](_rcp___response.md)中的调试信息的结构。

**起始版本：** 5.0.0(12)

### Rcp\_DnsConfiguration

```cpp
typedef struct Rcp_DnsConfiguration Rcp_DnsConfiguration
```

**描述**

DNS解析配置。

**起始版本：** 5.0.0(12)

### Rcp\_DnsOverHttps

```cpp
typedef struct Rcp_DnsOverHttps Rcp_DnsOverHttps
```

**描述**

如果设置了HTTPS上的DNS配置，则首选由DOH DNS服务器解析的地址。

**起始版本：** 5.0.0(12)

### Rcp\_DnsRule

```cpp
typedef struct Rcp_DnsRule Rcp_DnsRule
```

**描述**

DNS规则配置。

**起始版本：** 5.0.0(12)

### Rcp\_DnsRuleType

```cpp
typedef enum Rcp_DnsRuleType Rcp_DnsRuleType
```

**描述**

DNS规则类型。用于区分[Rcp\_DnsRule](_rcp___dns_rule.md)中使用的DNS规则类型。

**起始版本：** 5.0.0(12)

### Rcp\_DnsServers

```cpp
typedef struct Rcp_DnsServers Rcp_DnsServers
```

**描述**

DNS服务器。[Rcp\_DnsConfiguration.dnsRules](_rcp___dns_configuration.md#dnsrules)中的类型之一。

**起始版本：** 5.0.0(12)

### Rcp\_DynamicDnsRuleFunction

```cpp
typedef Rcp_IpAddress*(* Rcp_DynamicDnsRuleFunction) (const char *host, uint16_t port)
```

**描述**

一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| host | 主机名称。 |
| port | 端口号。 |

**返回：**

Rcp\_IpAddress\* 指向[Rcp\_IpAddress](_rcp___ip_address.md)的指针。基于主机名和端口的IP地址。

### Rcp\_EventsHandler

```cpp
typedef struct Rcp_EventsHandler Rcp_EventsHandler
```

**描述**

监听不同HTTP事件的回调函数。

**起始版本：** 5.0.0(12)

### Rcp\_ExclusionFunction

```cpp
typedef bool(* Rcp_ExclusionFunction) (const char *url)
```

**描述**

判断host是否使用代理的函数指针，true代表使用，false代表不使用。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| url | 请求的URL。 |

**返回：**

bool 返回是否使用代理。true代表使用，false代表不使用。

### Rcp\_Exclusions

```cpp
typedef struct Rcp_Exclusions Rcp_Exclusions
```

**描述**

代理配置中用于过滤不使用代理的URLs。

如果[Rcp\_Request.url](_rcp___request.md#url)匹配[Rcp\_Exclusions](_rcp___exclusions.md)规则，则[Rcp\_Request](_rcp___request.md)不会使用代理。

**起始版本：** 5.0.0(12)

### Rcp\_ExclusionsValueType

```cpp
typedef enum Rcp_ExclusionsValueType Rcp_ExclusionsValueType
```

**描述**

代理排除中使用的数据类型。用于区分[Rcp\_Exclusions](_rcp___exclusions.md)中使用的数据。

**起始版本：** 5.0.0(12)

### Rcp\_Form

```cpp
typedef struct Rcp_Form Rcp_Form
```

**描述**

简单表单。

**起始版本：** 5.0.0(12)

### Rcp\_FormFieldFileValue

```cpp
typedef struct Rcp_FormFieldFileValue Rcp_FormFieldFileValue
```

**描述**

表单字段文件值。

**起始版本：** 5.0.0(12)

### Rcp\_FormFieldValue

```cpp
typedef struct Rcp_FormFieldValue Rcp_FormFieldValue
```

**描述**

简单表单数据字段值，参见[Rcp\_Form](remote-communication-overview.md#rcp_form)和[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)。

**起始版本：** 5.0.0(12)

### Rcp\_FormValueType

```cpp
typedef enum Rcp_FormValueType Rcp_FormValueType
```

**描述**

表单值类型。

**起始版本：** 5.0.0(12)

### Rcp\_GetDataCallback

```cpp
typedef int(* Rcp_GetDataCallback) (char *out, uint32_t size)
```

**描述**

通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。

该回调可能使用在[Rcp\_FormFieldFileValue.contentOrPathOrCb](_rcp___form_field_file_value.md#contentorpathorcb)和[Rcp\_RequestContent](_rcp___request_content.md)中。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| out | 输出的数据 |
| size | 数据大小 |

**返回：**

int 返回值为-1表示错误，返回值0表示停止传输。

### Rcp\_HeaderEntry

```cpp
typedef struct Rcp_HeaderEntry Rcp_HeaderEntry
```

**描述**

请求或响应的标头的所有键值对。

**起始版本：** 5.0.0(12)

### Rcp\_Headers

```cpp
typedef struct Rcp_Headers Rcp_Headers
```

**描述**

请求或响应的标头。

**起始版本：** 5.0.0(12)

### Rcp\_HeaderValue

```cpp
typedef struct Rcp_HeaderValue Rcp_HeaderValue
```

**描述**

请求或响应的标头映射的值类型。

**起始版本：** 5.0.0(12)

### Rcp\_InfoToCollect

```cpp
typedef struct Rcp_InfoToCollect Rcp_InfoToCollect
```

**描述**

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

**起始版本：** 5.0.0(12)

### Rcp\_Interceptor

```cpp
typedef struct Rcp_Interceptor Rcp_Interceptor
```

**描述**

异步拦截器。

**起始版本：** 5.0.0(12)

### Rcp\_InterceptorArray

```cpp
typedef struct Rcp_InterceptorArray Rcp_InterceptorArray
```

**描述**

异步拦截器数组。

**起始版本：** 5.0.0(12)

### Rcp\_IpAddress

```cpp
typedef struct Rcp_IpAddress Rcp_IpAddress
```

**描述**

指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](_rcp___static_dns_rule_item.md)。

**起始版本：** 5.0.0(12)

### Rcp\_IpAndPort

```cpp
typedef struct Rcp_IpAndPort Rcp_IpAndPort
```

**描述**

该接口用在[Rcp\_DnsServers](_rcp___dns_servers.md)中，表示一个DNS服务器的地址和端口。

**起始版本：** 5.0.0(12)

### Rcp\_MultipartForm

```cpp
typedef struct Rcp_MultipartForm Rcp_MultipartForm
```

**描述**

多部分表单。

**起始版本：** 5.0.0(12)

### Rcp\_MultipartFormFieldValue

```cpp
typedef struct Rcp_MultipartFormFieldValue Rcp_MultipartFormFieldValue
```

**描述**

多部分表单域值，在[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)中使用。

**起始版本：** 5.0.0(12)

### Rcp\_MultipartValueType

```cpp
typedef enum Rcp_MultipartValueType Rcp_MultipartValueType
```

**描述**

多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)中使用的数据。

**起始版本：** 5.0.0(12)

### Rcp\_OnDataReceiveCallback

```cpp
typedef struct Rcp_OnDataReceiveCallback Rcp_OnDataReceiveCallback
```

**描述**

接收到数据时回调。[Rcp\_EventsHandler](_rcp___events_handler.md)中的配置。

**起始版本：** 5.0.0(12)

### Rcp\_OnDataReceiveCallbackFunc

```cpp
typedef size_t(* Rcp_OnDataReceiveCallbackFunc) (void *usrObject, const char *data)
```

**描述**

接收到响应正文时调用的回调函数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| data | 响应体。 |

**返回：**

size\_t 响应体的长度。

### Rcp\_OnBinaryReceiveCallback

```cpp
typedef struct Rcp_OnBinaryReceiveCallback Rcp_OnBinaryReceiveCallback
```

**描述**

响应的二进制数据接收回调函数。

**起始版本：** 5.0.1(13)

### Rcp\_OnBinaryReceiveCallbackFunc

```cpp
typedef size_t(* Rcp_OnBinaryReceiveCallbackFunc) (void *usrObject, Rcp_Buffer *buffer)
```

**描述**

接收到响应正文时调用的二进制回调函数。其回调点与[Rcp\_Configuration](_rcp___configuration.md)中配置的[Rcp\_OnDataReceiveCallback](remote-communication-overview.md#rcp_ondatareceivecallback)一致。设置后其回调函数会替换在[Rcp\_Configuration](_rcp___configuration.md)中配置的[Rcp\_OnDataReceiveCallback](remote-communication-overview.md#rcp_ondatareceivecallback)，功能上能够涵盖[Rcp\_OnDataReceiveCallback](remote-communication-overview.md#rcp_ondatareceivecallback)的字符数据接收获取功能。

**起始版本：** 5.0.1(13)

**参数:**

| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| buffer | 响应体的二进制数据。 |

**返回：**

size\_t 响应体二进制数据的长度。

### Rcp\_OnStatusCodeReceiveCallback

```cpp
typedef struct Rcp_OnStatusCodeReceiveCallback Rcp_OnStatusCodeReceiveCallback
```

**描述**

用于接收响应状态码的回调函数。

**起始版本：** 6.0.1(21)

### Rcp\_OnStatusCodeReceiveCallbackFunc

```cpp
typedef void (*Rcp_OnStatusCodeReceiveCallbackFunc) (void *usrObject, uint32_t statusCode)
```

**描述**

接收到响应状态码时调用的回调函数。

**起始版本：** 6.0.1(21)

**参数:**

| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| statusCode | 响应状态码。 |

### Rcp\_OnHeaderReceiveCallback

```cpp
typedef struct Rcp_OnHeaderReceiveCallback Rcp_OnHeaderReceiveCallback
```

**描述**

[Rcp\_EventsHandler](_rcp___events_handler.md)中配置的接收到的header的回调配置。

**起始版本：** 5.0.0(12)

### Rcp\_OnHeaderReceiveCallbackFunc

```cpp
typedef void(* Rcp_OnHeaderReceiveCallbackFunc) (void *usrObject, Rcp_Headers *headers)
```

**描述**

收到所有请求时调用的回调。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| headers | 接收到的请求头，指向[Rcp\_Headers](remote-communication-overview.md#rcp_headers)的指针。 |

### Rcp\_OnProgressCallback

```cpp
typedef struct Rcp_OnProgressCallback Rcp_OnProgressCallback
```

**描述**

收发时回调配置，在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置。

**起始版本：** 5.0.0(12)

### Rcp\_OnProgressCallbackFunc

```cpp
typedef void(* Rcp_OnProgressCallbackFunc) (void *usrObject, uint64_t totalSize, uint64_t transferredSize)
```

**描述**

请求/响应数据传输过程中调用的回调函数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| totalSize | 数据总大小。 |
| transferredSize | 已传输的数据大小。 |

### Rcp\_OnVoidCallback

```cpp
typedef struct Rcp_OnVoidCallback Rcp_OnVoidCallback
```

**描述**

在[Rcp\_EventsHandler](_rcp___events_handler.md)中配置的数据结束或已取消事件的回调配置。

**起始版本：** 5.0.0(12)

### Rcp\_OnVoidCallbackFunc

```cpp
typedef void(* Rcp_OnVoidCallbackFunc) (void *usrObject)
```

**描述**

请求的DataEnd或Canceled事件回调的回调函数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |

### Rcp\_PathPreference

```cpp
typedef enum Rcp_PathPreference Rcp_PathPreference
```

**描述**

请求路径首选项。

调用者的建议，最终由系统决定使用哪个路径。

**起始版本：** 5.0.0(12)

### Rcp\_ProxyConfiguration

```cpp
typedef struct Rcp_ProxyConfiguration Rcp_ProxyConfiguration
```

**描述**

代理配置。

**起始版本：** 5.0.0(12)

### Rcp\_ProxyTunnelMode

```cpp
typedef enum Rcp_ProxyTunnelMode Rcp_ProxyTunnelMode
```

**描述**

用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。'auto'表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。

**起始版本：** 5.0.0(12)

### Rcp\_ProxyType

```cpp
typedef enum Rcp_ProxyType Rcp_ProxyType
```

**描述**

代理类型。用于区分不同的代理配置。

**起始版本：** 5.0.0(12)

### Rcp\_RemoteValidationType

```cpp
typedef enum Rcp_RemoteValidationType Rcp_RemoteValidationType
```

**描述**

远程验证类型。

用于区分验证远程服务器身份的CA，在[Rcp\_SecurityConfiguration](_rcp___security_configuration.md)中描述。

**起始版本：** 5.0.0(12)

### Rcp\_Request

```cpp
typedef struct Rcp_Request Rcp_Request
```

**描述**

网络请求。

**起始版本：** 5.0.0(12)

### Rcp\_FormOrder

```cpp
typedef struct Rcp_FormOrder Rcp_FormOrder
```

**描述**

表单键值对发送顺序。

**起始版本：** 26.0.0

### Rcp\_RequestContent

```cpp
typedef struct Rcp_RequestContent Rcp_RequestContent
```

**描述**

请求的内容。

**起始版本：** 5.0.0(12)

### Rcp\_RequestCookieEntry

```cpp
typedef struct Rcp_RequestCookieEntry Rcp_RequestCookieEntry
```

**描述**

描述请求的所有Cookie键值对。

**起始版本：** 5.0.0(12)

### Rcp\_RequestCookies

```cpp
typedef struct Rcp_RequestCookies Rcp_RequestCookies
```

**描述**

请求Cookie。

允许你在一个对象中指定你需要的所有Cookies，例如：{'name1'：'value1'，'name2'：'value2'}。

**起始版本：** 5.0.0(12)

### Rcp\_RequestHandler

```cpp
typedef struct Rcp_RequestHandler Rcp_RequestHandler
```

**描述**

与[Rcp\_Interceptor](_rcp___interceptor.md)关联的异步处理器。

**起始版本：** 5.0.0(12)

### Rcp\_Response

```cpp
typedef struct Rcp_Response Rcp_Response
```

**描述**

网络请求的响应。

**起始版本：** 5.0.0(12)

### Rcp\_ResponseCallback

```cpp
typedef void(* Rcp_ResponseCallback) (void *usrCtx, Rcp_Response *response, uint32_t errCode)
```

**描述**

响应回调函数指针。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| usrCtx | 用户上下文。 |
| response | 请求所生成的响应。指向[Rcp\_Response](_rcp___response.md)的指针。 |
| errCode | [out] 表示常见的错误代码。  0：成功。  [1007900001](errorcode-remote-communication.md#section1007900001-不支持的协议)：不支持的协议。  [1007900003](errorcode-remote-communication.md#section1007900003-url格式错误)：URL使用了错误/非法的格式或缺少URL。  [1007900005](errorcode-remote-communication.md#section1007900005-代理服务器域名解析失败)：无法解析代理名称。  [1007900006](errorcode-remote-communication.md#section1007900006-域名解析失败)：无法解析主机名。  [1007900007](errorcode-remote-communication.md#section1007900007-无法连接到服务器)：无法连接到服务器。  [1007900008](errorcode-remote-communication.md#section1007900008-服务器返回非法数据)：异常的服务器回复。  [1007900009](errorcode-remote-communication.md#section1007900009-拒绝对远程资源的访问)：对远程资源的访问被拒绝。  [1007900016](errorcode-remote-communication.md#section1007900016-http2帧层错误)：HTTP2框架层中的错误。  [1007900018](errorcode-remote-communication.md#section1007900018-服务器返回数据不完整)：已传输部分文件。  [1007900025](errorcode-remote-communication.md#section1007900025-上传失败)：上载失败。  [1007900026](errorcode-remote-communication.md#section1007900026-从文件应用程序中打开读取本地数据失败)：无法从文件/应用程序中打开/读取本地数据。  [1007900027](errorcode-remote-communication.md#section1007900027-内存不足)：内存不足。  [1007900028](errorcode-remote-communication.md#section1007900028-操作超时)：已达到超时。  [1007900047](errorcode-remote-communication.md#section1007900047-重定向次数达到最大值)：重定向数达到最大数量。  [1007900052](errorcode-remote-communication.md#section1007900052-服务器没有返回内容)：服务器没有返回任何内容（没有标头，没有数据）。  [1007900055](errorcode-remote-communication.md#section1007900055-发送网络数据失败)：向对等方发送数据失败。  [1007900056](errorcode-remote-communication.md#section1007900056-接收网络数据失败)：从对等方接收数据时失败。  [1007900058](errorcode-remote-communication.md#section1007900058-本地ssl证书错误)：本地SSL证书有问题。  [1007900059](errorcode-remote-communication.md#section1007900059-无法使用指定的密码)：无法使用指定的SSL密钥。  [1007900060](errorcode-remote-communication.md#section1007900060-远程服务器ssl证书或ssh秘钥不正确)：SSL对等证书或SSH远程密钥不正常。  [1007900061](errorcode-remote-communication.md#section1007900061-无法识别或错误的http编码格式)：无法识别或错误的HTTP内容或传输编码。  [1007900063](errorcode-remote-communication.md#section1007900063-超出最大文件大小)：超过了最大文件大小。  [1007900070](errorcode-remote-communication.md#section1007900070-服务器磁盘空间不足)：磁盘已满或分配超出。  [1007900073](errorcode-remote-communication.md#section1007900073-服务器返回文件已存在)：远程文件已存在。  [1007900077](errorcode-remote-communication.md#section1007900077-ssl-ca证书不存在或没有访问权限)：SSL CA证书有问题 (路径？ 访问权限？)。  [1007900078](errorcode-remote-communication.md#section1007900078-url请求的文件不存在)：找不到远程文件。  [1007900992](errorcode-remote-communication.md#section1007900992-请求已被取消)：请求已取消。  [1007900993](errorcode-remote-communication.md#section1007900993-会话已关闭)：会话已关闭或无效。  [1007900094](errorcode-remote-communication.md#section1007900094-身份校验失败)：身份验证函数返回了错误。  [1007900201](errorcode-remote-communication.md#section1007900201-禁止明文传输)：禁止明文传输。从6.1.0(23)版本开始新增支持此错误码。  [1007900995](errorcode-remote-communication.md#section1007900995-获取系统代理失败)：获取系统代理失败。  [1007900996](errorcode-remote-communication.md#section1007900996-代理类型不支持)：代理类型不受支持。  [1007900997](errorcode-remote-communication.md#section1007900997-无效的内容类型)：无效的内容类型。  [1007900998](errorcode-remote-communication.md#section1007900998-所请求的方法不被支持)：方法不受支持。  [1007900999](errorcode-remote-communication.md#section1007900999-内部错误)：内部错误。  Others：1007900000 + CURL\_ERROR\_CODE。 更多常见的错误码，请参见[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)。 |

### Rcp\_ResponseCallbackObject

```cpp
typedef struct Rcp_ResponseCallbackObject Rcp_ResponseCallbackObject
```

**描述**

响应回调结构体。

**起始版本：** 5.0.0(12)

### Rcp\_ResponseCookies

```cpp
typedef struct Rcp_ResponseCookies Rcp_ResponseCookies
```

**描述**

响应Cookie。

**起始版本：** 5.0.0(12)

### Rcp\_SecurityConfiguration

```cpp
typedef struct Rcp_SecurityConfiguration Rcp_SecurityConfiguration
```

**描述**

请求的安全配置。

**起始版本：** 5.0.0(12)

### Rcp\_ServerAuthentication

```cpp
typedef struct Rcp_ServerAuthentication Rcp_ServerAuthentication
```

**描述**

服务器身份验证。

**起始版本：** 5.0.0(12)

### Rcp\_Session

```cpp
typedef struct Rcp_Session Rcp_Session
```

**描述**

会话。

**起始版本：** 5.0.0(12)

### Rcp\_SessionConfiguration

```cpp
typedef struct Rcp_SessionConfiguration Rcp_SessionConfiguration
```

**描述**

会话配置。

**起始版本：** 5.0.0(12)

### Rcp\_SessionListener

```cpp
typedef struct Rcp_SessionListener Rcp_SessionListener
```

**描述**

关闭或取消会话事件的回调函数。

**起始版本：** 5.0.0(12)

### Rcp\_SessionType

```cpp
typedef enum Rcp_SessionType Rcp_SessionType
```

**描述**

会话类型。

**起始版本：** 5.0.0(12)

### Rcp\_StaticDnsRule

```cpp
typedef struct Rcp_StaticDnsRule Rcp_StaticDnsRule
```

**描述**

静态DNS规则。

**起始版本：** 5.0.0(12)

### Rcp\_StaticDnsRuleItem

```cpp
typedef struct Rcp_StaticDnsRuleItem Rcp_StaticDnsRuleItem
```

**描述**

描述单个静态DNS规则。

**起始版本：** 5.0.0(12)

### Rcp\_StatusCode

```cpp
typedef enum Rcp_StatusCode Rcp_StatusCode
```

**描述**

请求响应的状态码。

**起始版本：** 5.0.0(12)

### Rcp\_SyncInterceptor

```cpp
typedef struct Rcp_SyncInterceptor Rcp_SyncInterceptor
```

**描述**

同步拦截器。

**起始版本：** 5.0.0(12)

### Rcp\_SyncInterceptorArray

```cpp
typedef struct Rcp_SyncInterceptorArray Rcp_SyncInterceptorArray
```

**描述**

同步拦截器数组。

**起始版本：** 5.0.0(12)

### Rcp\_SyncRequestHandler

```cpp
typedef struct Rcp_SyncRequestHandler Rcp_SyncRequestHandler
```

**描述**

与[Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)关联的同步处理器。

**起始版本：** 5.0.0(12)

### Rcp\_TimeInfo

```cpp
typedef struct Rcp_TimeInfo Rcp_TimeInfo
```

**描述**

响应计时信息。

它将在[Rcp\_Response.timeInfo](_rcp___response.md#timeinfo)中被收集，[Rcp\_TracingConfiguration.collectTimeInfo](_rcp___tracing_configuration.md#collecttimeinfo)决定是否收集它。

**起始版本：** 5.0.0(12)

### Rcp\_Timeout

```cpp
typedef struct Rcp_Timeout Rcp_Timeout
```

**描述**

请求的超时配置。

**起始版本：** 5.0.0(12)

### Rcp\_TracingConfiguration

```cpp
typedef struct Rcp_TracingConfiguration Rcp_TracingConfiguration
```

**描述**

请求追踪配置。

**起始版本：** 5.0.0(12)

### Rcp\_TransferConfiguration

```cpp
typedef struct Rcp_TransferConfiguration Rcp_TransferConfiguration
```

**描述**

传输配置。

**起始版本：** 5.0.0(12)

### Rcp\_TransferRange

```cpp
typedef struct Rcp_TransferRange Rcp_TransferRange
```

**描述**

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

**起始版本：** 5.0.0(12)

### Rcp\_Urls

```cpp
typedef struct Rcp_Urls Rcp_Urls
```

**描述**

URLs，用于确定主机是否正在使用代理。

**起始版本：** 5.0.0(12)

### Rcp\_WebProxy

```cpp
typedef struct Rcp_WebProxy Rcp_WebProxy
```

**描述**

自定义代理配置。

**起始版本：** 5.0.0(12)

### Rcp\_OnGetDataCallback

```cpp
typedef struct Rcp_OnGetDataCallback  Rcp_OnGetDataCallback
```

**描述**

获取数据的回调。

**起始版本：** 26.0.0

### Rcp\_GetDataCallbackFunc

```cpp
typedef size_t(* Rcp_GetDataCallbackFunc) (void *userObject, uint8_t *outData, size_t size)
```

**描述**

获取数据的回调函数。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| userObject | 用户定义的对象。 |
| outData | 输出数据的缓冲区。 |
| size | 缓冲区长度。 |

**返回：**

size\_t 发送的数据长度。

### Rcp\_QuicConn

```cpp
typedef void Rcp_QuicConn
```

**描述**

quic连接实例的类型。

**起始版本：** 26.0.0

### Rcp\_QuicSession

```cpp
typedef void Rcp_QuicSession
```

**描述**

quic会话的类型，可以管理多个连接实例。

**起始版本：** 26.0.0

### Rcp\_QuicSlist

```cpp
typedef struct Rcp_QuicSlist Rcp_QuicSlist
```

**描述**

链表数据结构。

**起始版本：** 26.0.0

### Rcp\_QuicIpAddress

```cpp
typedef struct Rcp_QuicIpAddress Rcp_QuicIpAddress
```

**描述**

用于存储IP地址的数据结构。

**起始版本：** 26.0.0

### Rcp\_QuicDynamicDnsRuleFunction

```cpp
typedef Rcp_QuicIpAddress (*Rcp_QuicDynamicDnsRuleFunction)(Rcp_QuicConn *conn, void *userObject, const char *host, uint16_t port)
```

**描述**

自定义DNS解析回调函数，根据主机名和端口返回IP地址。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| host | 请求的主机名。 |
| port | 请求的端口号。 |

**返回：**

[Rcp\_QuicIpAddress](remote-communication-overview.md#rcp_quicipaddress) 根据主机名和端口解析的IP地址。

### Rcp\_QuicIoVec

```cpp
typedef struct Rcp_QuicIoVec Rcp_QuicIoVec
```

**描述**

用于存储二进制内容的数据结构。

**起始版本：** 26.0.0

### Rcp\_QuicStreamData

```cpp
typedef struct Rcp_QuicStreamData Rcp_QuicStreamData
```

**描述**

quic连接中用于接收流式数据的存储结构。

**起始版本：** 26.0.0

### Rcp\_QuicConnectionOnCertAuthority

```cpp
typedef Rcp_QuicErrorCode (*Rcp_QuicConnectionOnCertAuthority)(Rcp_QuicConn *conn, void *userObject, const unsigned char *const *certs, const size_t *certLens, size_t certsCount)
```

**描述**

证书校验的回调函数。在quic建链时，用于自定义校验对端证书。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| certs | X509证书数组（DER格式）。 |
| certLens | 每个证书的长度数组。 |
| certsCount | 证书数量。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) ：自定义证书验证结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS为验证通过，其余返回值均为验证失败。

### Rcp\_QuicConnectionOnSessionTicketUpdate

```cpp
typedef void (*Rcp_QuicConnectionOnSessionTicketUpdate)(Rcp_QuicConn *conn, void *userObject, const char *sessionTicket, size_t length)
```

**描述**

quic会话票据更新回调函数。在quic会话中票据更新时触发，返回新的票据。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| sessionTicket | quic会话票据内容。 |
| length | 会话票据长度。 |

### Rcp\_QuicConnectionOnConnected

```cpp
typedef void (*Rcp_QuicConnectionOnConnected)(Rcp_QuicConn *conn, void *userObject)
```

**描述**

quic连接成功回调函数。quic连接成功建立时触发该函数。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |

### Rcp\_QuicConnectionOnError

```cpp
typedef void (*Rcp_QuicConnectionOnError)(Rcp_QuicConn *conn, void *userObject, Rcp_QuicErrorCode errCode, const char *errDetail)
```

**描述**

quic连接失败回调函数。quic连接建立失败时触发该函数，返回失败原因。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| errCode | 建立quic连接失败错误码。 |
| errDetail | 错误详细信息。 |

### Rcp\_QuicConnectionOnClosed

```cpp
typedef void (*Rcp_QuicConnectionOnClosed)(Rcp_QuicConn *conn, void *userObject)
```

**描述**

quic连接关闭回调函数。quic连接关闭时触发，通知连接已关闭。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |

### Rcp\_QuicConnectionOnStreamInbound

```cpp
typedef void (*Rcp_QuicConnectionOnStreamInbound)(Rcp_QuicConn *conn, void *userObject, uint64_t streamId)
```

**描述**

quic连接中入站流回调函数。当quic连接中对端创建流时触发，处理对端发起的流，设置流的选项和回调。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| streamId | 入站流的ID。 |

### Rcp\_QuicStreamOnEvent

```cpp
typedef void (*Rcp_QuicStreamOnEvent)(Rcp_QuicConn *conn, void *userObject, uint64_t streamId, Rcp_QuicErrorCode errCode, const char *errDetail)
```

**描述**

quic连接中流事件回调函数。当quic连接中的流发生事件时触发，用于处理流的状态变化和错误。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| streamId | 入站流的ID。 |
| errCode | 建立quic连接失败错误码。 |
| errDetail | 错误详细信息。 |

### Rcp\_QuicStreamOnReceiveData

```cpp
typedef uint64_t (*Rcp_QuicStreamOnReceiveData)(Rcp_QuicConn *conn, void *userObject, uint64_t streamId, const Rcp_QuicStreamData *streamData)
```

**描述**

quic连接中流数据接收回调函数。当quic连接中接收到流数据时触发，用于处理接收到的数据。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| streamId | quic流的ID。 |
| streamData | quic流数据。 |

**返回：**

uint64\_t ：quic流接收数据的字节数。

## 枚举类型说明

### Rcp\_AuthenticationType

```cpp
enum Rcp_AuthenticationType
```

**描述**

枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_AUTHENTICATION\_AUTO | 自动 |
| RCP\_AUTHENTICATION\_BASIC | 基本类型 |
| RCP\_AUTHENTICATION\_NTLM | NTLM类型 |
| RCP\_AUTHENTICATION\_DIGEST | DIGEST类型 |

### Rcp\_CertType

```cpp
enum Rcp_CertType
```

**描述**

客户端证书类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_CERT\_PEM | PEM证书类型。 |
| RCP\_CERT\_DER | DER证书类型。 |
| RCP\_CERT\_P12 | P12证书类型。 |

### Rcp\_ContentOrPathOrCallbackType

```cpp
enum Rcp_ContentOrPathOrCallbackType
```

**描述**

回调的内容、路径或类型。用于区分[Rcp\_ContentOrPathOrCallback](_rcp___content_or_path_or_callback.md)中使用的数据。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_FILE\_VALUE\_TYPE\_CONTENT | 表示内容类型。 |
| RCP\_FILE\_VALUE\_TYPE\_PATH | 表示路径类型。 |
| RCP\_FILE\_VALUE\_TYPE\_CALLBACK | 表示回调类型。 |

### Rcp\_ContentType

```cpp
enum Rcp_ContentType
```

**描述**

内容类型。用于区分[Rcp\_RequestContent](_rcp___request_content.md)中使用的数据。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_CONTENT\_TYPE\_STRING | 文本。 |
| RCP\_CONTENT\_TYPE\_FORM | 表格。 |
| RCP\_CONTENT\_TYPE\_MULTIPARTFORM | 多部分表格。 |
| RCP\_CONTENT\_TYPE\_GETCALLBACK | 回调函数。 |

### Rcp\_DebugEvent

```cpp
enum Rcp_DebugEvent
```

**描述**

描述调试信息的事件类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_DEBUG\_EVENT\_TEXT | 文本事件。 |
| RCP\_DEBUG\_EVENT\_HEADER\_IN | 传入标头事件。 |
| RCP\_DEBUG\_EVENT\_HEADER\_OUT | 传出标头事件。 |
| RCP\_DEBUG\_EVENT\_DATA\_IN | 接收数据事件。 |
| RCP\_DEBUG\_EVENT\_DATA\_OUT | 外发数据事件。 |
| RCP\_DEBUG\_EVENT\_SSL\_DATA\_IN | 传入SSL/TLS事件。 |
| RCP\_DEBUG\_EVENT\_SSL\_DATA\_OUT | 传出SSL/TLS事件。 |

### Rcp\_DnsRuleType

```cpp
enum Rcp_DnsRuleType
```

**描述**

DNS规则类型。用于区分[Rcp\_DnsRule](_rcp___dns_rule.md)中使用的DNS规则类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_DNS\_RULE\_DNS\_SERVERS | DNS服务器。 |
| RCP\_DNS\_RULE\_STATIC | 静态DNS规则。 |
| RCP\_DNS\_RULE\_DYNAMIC | 动态DNS规则。 |

### Rcp\_ExclusionsValueType

```cpp
enum Rcp_ExclusionsValueType
```

**描述**

代理排除中使用的数据类型，用于区分[Rcp\_Exclusions](_rcp___exclusions.md)中使用的数据。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_EXCLUSION\_USE\_URL\_ARRAY | 表示在[Rcp\_Exclusions](_rcp___exclusions.md)中使用urls。 |
| RCP\_EXCLUSION\_USE\_CALLBACK | 在[Rcp\_Exclusions](_rcp___exclusions.md)中使用回调函数[Rcp\_ExclusionFunction](remote-communication-overview.md#rcp_exclusionfunction)。 |

### Rcp\_FormValueType

```cpp
enum Rcp_FormValueType
```

**描述**

表单值类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_FORM\_VALUE\_TYPE\_INT32 | 表示INT32数据类型。 |
| RCP\_FORM\_VALUE\_TYPE\_INT64 | 表示INT64数据类型。 |
| RCP\_FORM\_VALUE\_TYPE\_BOOL | 表示bool数据类型。 |
| RCP\_FORM\_VALUE\_TYPE\_STRING | 表示string数据类型。 |
| RCP\_FORM\_VALUE\_TYPE\_DOUBLE | 表示double数据类型。 |

### Rcp\_MultipartValueType

```cpp
enum Rcp_MultipartValueType
```

**描述**

多部分值类型。用于区分[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)中使用的数据。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_TYPE\_FORM\_FIELD\_VALUE | 表示使用[Rcp\_FormFieldValue](_rcp___form_field_value.md)。 |
| RCP\_TYPE\_FORM\_FIELD\_FILE\_VALUE | 表示使用[Rcp\_FormFieldFileValue](_rcp___form_field_file_value.md)。 |

### Rcp\_PathPreference

```cpp
enum Rcp_PathPreference
```

**描述**

请求路径首选项。

这只是调用者的建议，系统决定使用哪个路径。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_PATH\_PREFERENCE\_AUTO | 自动。 |
| RCP\_PATH\_PREFERENCE\_WIFI | 倾向WIFI网络。 |
| RCP\_PATH\_PREFERENCE\_CELLULAR | 倾向蜂窝网路。 |

### Rcp\_ProxyTunnelMode

```cpp
enum Rcp_ProxyTunnelMode
```

**描述**

用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_PROXY\_TUNNEL\_AUTO | 自动。 |
| RCP\_PROXY\_TUNNEL\_ALWAYS | 总是创建。 |

### Rcp\_ProxyType

```cpp
enum Rcp_ProxyType
```

**描述**

代理类型。用于区分不同的代理配置。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_PROXY\_SYSTEM | 系统代理。 |
| RCP\_PROXY\_CUSTOM | 使用自定义代理，选择后将解析[Rcp\_ProxyConfiguration.customProxy](_rcp___proxy_configuration.md#customproxy)。 |
| RCP\_PROXY\_NO\_PROXY | 不使用代理。 |

### Rcp\_RemoteValidationType

```cpp
enum Rcp_RemoteValidationType
```

**描述**

远程验证类型。

用于区分验证远程服务器身份的CA在[Rcp\_SecurityConfiguration](_rcp___security_configuration.md)中描述。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_REMOTE\_VALIDATION\_SYSTEM | 系统验证。 |
| RCP\_REMOTE\_VALIDATION\_SKIP | 跳过验证。 |
| RCP\_REMOTE\_VALIDATION\_CERTIFICATE\_AUTHORITY | CA验证。 |

### Rcp\_SessionType

```cpp
enum Rcp_SessionType
```

**描述**

会话类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_SESSION\_TYPE\_HTTP = 0 | 使用HTTP会话。 |
| RCP\_SESSION\_TYPE\_MAX = 100 | Rcp\_SessionType的最大值。 |

### Rcp\_StatusCode

```cpp
enum Rcp_StatusCode
```

**描述**

请求响应的状态码。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| RCP\_NONE = 0 | 默认值。 |
| RCP\_OK = 200 | 请求成功。 |
| RCP\_CREATED = 201 | 请求成功并创建了新资源。 |
| RCP\_ACCEPTED = 202 | 请求已接受，但尚未处理。 |
| RCP\_NOT\_AUTHORITATIVE = 203 | 返回信息不是原始的。 |
| RCP\_NO\_CONTENT = 204 | 请求成功，但无返回内容。 |
| RCP\_RESET= 205 | 请求已成功处理，但需要重置内容。 |
| RCP\_PARTIAL = 206 | 部分内容请求成功。 |
| RCP\_MULTI\_CHOICE = 300 | 对于该请求，服务器支持多种操作方式。 |
| RCP\_MOVED\_PERMANENTLY = 301 | 永久重定向。 |
| RCP\_MOVED\_TEMPORARILY = 302 | 临时重定向。 |
| RCP\_SEE\_OTHER = 303 | 查看其他位置。 |
| RCP\_NOT\_MODIFIED = 304 | 资源未修改。 |
| RCP\_USE\_PROXY = 305 | 使用代理。 |
| RCP\_BAD\_REQUEST = 400 | 请求语法错误。 |
| RCP\_UNAUTHORIZED = 401 | 未授权。 |
| RCP\_PAYMENT\_REQUIRED = 402 | 需要付费。 |
| RCP\_FORBIDDEN = 403 | 禁止访问。 |
| RCP\_NOT\_FOUND = 404 | 资源未找到。 |
| RCP\_BAD\_METHOD = 405 | 方法不允许。 |
| RCP\_NOT\_ACCEPTABLE = 406 | 不接受。 |
| RCP\_PROXY\_AUTH = 407 | 需要代理授权。 |
| RCP\_CLIENT\_TIMEOUT = 408 | 请求超时。 |
| RCP\_CONFLICT = 409 | 冲突。 |
| RCP\_GONE = 410 | 资源已永久删除。 |
| RCP\_LENGTH\_REQUIRED = 411 | 需要有效长度。 |
| RCP\_PRECON\_FAILED = 412 | 未满足前提条件。 |
| RCP\_ENTITY\_TOO\_LARGE = 413 | 请求实体过大。 |
| RCP\_REQ\_TOO\_LONG = 414 | 请求的 URI 过长。 |
| RCP\_UNSUPPORTED\_TYPE = 415 | 不支持的媒体类型。 |
| RCP\_INTERNAL\_ERROR = 500 | 服务器内部错误。 |
| RCP\_NOT\_IMPLEMENTED = 501 | 尚未实现。 |
| RCP\_BAD\_GATEWAY = 502 | 网关错误。 |
| RCP\_UNAVAILABLE = 503 | 服务不可用。 |
| RCP\_GATEWAY\_TIMEOUT = 504 | 网关超时。 |
| RCP\_VERSION = 505 | 不支持的HTTP版本。 |

### RCP\_QuicIpResolve

```cpp
enum RCP_QuicIpResolve
```

**描述**

请求DNS解析时使用的IP解析类型。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| RCP\_QUIC\_IP\_RESOLVE\_WHATEVER = 0 | 使用IPv4地址或者IPv6地址。默认值。 |
| RCP\_QUIC\_IP\_RESOLVE\_V4 | 仅使用IPv4地址。 |
| RCP\_QUIC\_IP\_RESOLVE\_V6 | 仅使用IPv6地址。 |

### Rcp\_QuicConnOpt

```cpp
enum Rcp_QuicConnOpt
```

**描述**

quic连接选项类型，用于配置连接的各种参数和回调函数。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| RCP\_QUIC\_CONN\_IP\_ADDRESS = 0 | 配置quic建立连接时使用的IP地址。 |
| RCP\_QUIC\_CONN\_IP\_RESOLVE = 1 | 配置quic建立连接时使用的IP地址类型。 |
| RCP\_QUIC\_CONN\_DNS\_FUNCTION = 2 | 配置自定义DNS解析函数。 |
| RCP\_QUIC\_CONN\_ON\_CONNECTED\_FUNCTION = 3 | 配置quic连接成功建立时的回调函数。 |
| RCP\_QUIC\_CONN\_ON\_ERROR\_FUNCTION = 4 | 配置quic连接发生错误时的回调函数。 |
| RCP\_QUIC\_CONN\_ON\_CLOSED\_FUNCTION = 5 | 配置quic连接关闭时的回调函数。 |
| RCP\_QUIC\_CONN\_STREAM\_INBOUND\_FUNCTION = 6 | 配置quic连接接收到入站流时的回调函数。 |
| RCP\_QUIC\_CONN\_CONNECT\_TIMEOUT\_MS = 7 | 配置quic连接连接超时时间（ms）参数。 |
| RCP\_QUIC\_CONN\_IDLE\_TIMEOUT\_MS = 8 | 配置quic连接空闲超时时间（ms）参数。 |
| RCP\_QUIC\_TLS\_CERT\_AUTHORITY\_FUNCTION = 1000 | 配置quic连接证书验证时的回调函数。 |
| RCP\_QUIC\_TLS\_CERT\_AUTHORITY\_CONTENT = 1001 | 配置quic连接用于验证对端的CA证书。 |
| RCP\_QUIC\_TLS\_SESSION\_TICKET\_UPDATE\_FUNCTION = 1002 | 配置quic会话票据更新时的回调函数。 |
| RCP\_QUIC\_TLS\_SESSION\_TICKET\_CONTENT = 1003 | 配置quic会话票据内容参数。 |
| RCP\_QUIC\_TP\_INITIAL\_MAX\_BIDIRECTIONAL\_STREAMS = 2000 | 配置quic连接的初始最大双向流数传输参数。 |
| RCP\_QUIC\_TP\_INITIAL\_MAX\_DATA = 2001 | 配置quic连接的初始最大数据量传输参数。 |
| RCP\_QUIC\_TP\_INITIAL\_MAX\_STREAMDATA\_BIDIRECTIONAL\_LOCAL = 2002 | 配置quic连接的初始最大双向流本地数据量传输参数。 |
| RCP\_QUIC\_TP\_INITIAL\_MAX\_STREAMDATA\_BIDIRECTIONAL\_REMOTE = 2003 | 配置quic连接的初始最大双向流远程数据量传输参数。 |
| RCP\_QUIC\_TP\_INITIAL\_MAX\_STREAMDATA\_UNIDIRECTIONAL = 2004 | 配置quic连接的初始最大单向流数据量传输参数。 |
| RCP\_QUIC\_TP\_INITIAL\_MAX\_UNIDIRECTIONAL\_STREAMS = 2005 | 配置quic连接的初始最大单向流数传输参数。 |

### Rcp\_QuicStreamOpt

```cpp
enum Rcp_QuicStreamOpt
```

**描述**

quic流选项类型，用于配置流的各种参数和回调函数。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| RCP\_QUIC\_STREAM\_EVENT\_FUNCTION = 0 | 配置quic流事件发生时的回调函数。 |
| RCP\_QUIC\_STREAM\_DATA\_FUNCTION = 1 | 配置quic流数据接收时的回调函数。 |
| RCP\_QUIC\_INBOUND\_STREAM\_USER\_OBJECT = 2 | 配置入站QUIC流的用户对象。 |
| RCP\_QUIC\_STREAM\_SND\_BUFFER\_SIZE\_KB = 3 | 设置quic流发送缓冲区大小（KB）参数。 |

### Rcp\_QuicConnInfo

```cpp
enum Rcp_QuicConnInfo
```

**描述**

quic连接信息类型。用于查询连接的各种信息。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| RCP\_INFO\_CONN\_GET\_LOCALADDR = 0 | 获取quic连接的本地IP地址。 |
| RCP\_INFO\_CONN\_GET\_PEERADDR = 1 | 获取quic连接的对端IP地址。 |
| RCP\_INFO\_CONN\_DNS\_TIME\_MS = 2 | 获取quic连接的DNS解析时间（ms）。 |
| RCP\_INFO\_CONN\_CONNECT\_TIME\_MS = 3 | 获取quic连接的连接时间（ms）。 |
| RCP\_INFO\_CONN\_SCID = 4 | 获取quic连接的源CID（Source Connection ID）。 |
| RCP\_INFO\_CONN\_DCID = 5 | 获取quic连接的目标CID（Destination Connection ID）。 |

### Rcp\_QuicStreamInfo

```cpp
enum Rcp_QuicStreamInfo
```

**描述**

quic流信息类型。用于查询流的各种信息。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| RCP\_INFO\_STREAM\_SND\_BUFFER\_SIZE\_KB = 0 | 获取quic流的发送缓冲区大小（KB）。 |

### Rcp\_QuicErrorCode

```cpp
enum Rcp_QuicErrorCode
```

**描述**

quic请求中可能出现的错误码。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| RCP\_QUIC\_ERROR\_CODE\_SUCCESS = 0 | 操作成功。 |
| RCP\_QUIC\_PERMISSION\_DENIED = 201 | 权限被拒绝，需要ohos.permission.INTERNET权限。 |
| RCP\_QUIC\_ERROR\_CODE\_FAILED = 1007920001 | quic相关操作失败。 |
| RCP\_QUIC\_ERROR\_CODE\_INVALID\_PARAM = 1007920002 | 无效参数，传入的参数不符合要求。 |
| RCP\_QUIC\_ERROR\_CODE\_INVALID\_STATE = 1007920003 | 无效连接状态，当前状态下不允许执行该操作。 |
| RCP\_QUIC\_ERROR\_CODE\_OUT\_OF\_MEM = 1007920004 | 内存不足，无法分配所需内存。 |
| RCP\_QUIC\_ERROR\_CODE\_CLOSE\_FROM\_PEER = 1007920005 | quic连接被对端关闭。 |
| RCP\_QUIC\_ERROR\_CODE\_HANDSHAKE\_TIMEOUT = 1007920006 | quic连接握手超时。 |
| RCP\_QUIC\_ERROR\_CODE\_NETWORK\_IDLE\_TIMEOUT = 1007920007 | quic连接网络空闲超时。 |
| RCP\_QUIC\_ERROR\_INVALID\_FRAME = 1007920008 | quic连接接收到无效帧。 |
| RCP\_QUIC\_ERROR\_CODE\_SEND\_PENDING = 1007920009 | quic连接发送挂起，缓冲区已满。 |
| RCP\_QUIC\_ERROR\_CODE\_FINALIZE\_PENDING = 1007920010 | quic连接关闭挂起。 |
| RCP\_QUIC\_ERROR\_CODE\_NETWORK\_UNREACHABLE = 1007920011 | 网络不可达。 |
| RCP\_QUIC\_ERROR\_CODE\_ENCRYPT\_ERROR = 1007920012 | 加密错误，TLS握手或数据加密失败。 |
| RCP\_QUIC\_ERROR\_CODE\_BUFFER\_TOO\_SMALL = 1007920013 | 内部缓冲区过小。 |
| RCP\_QUIC\_ERROR\_CODE\_EAGAIN = 1007920015 | 非阻塞I/O操作资源暂时不可用，应稍后重试。 |
| RCP\_QUIC\_ERROR\_CODE\_STREAM\_CLOSED = 1007920018 | quic流已关闭。 |
| RCP\_QUIC\_ERROR\_CODE\_STREAM\_RESET\_RECEIVED = 1007920019 | quic流被对端重置。 |
| RCP\_QUIC\_ERROR\_CODE\_STREAM\_STOP\_SENDING\_RECEIVED = 1007920020 | quic流接收到停止发送请求。 |

### Rcp\_QuicStreamDirection

```cpp
enum Rcp_QuicStreamDirection
```

**描述**

quic流的方向类型。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| RCP\_QUIC\_STREAM\_BIDI = 0 | 双向流，流的两端都可以发送和接收数据。 |
| RCP\_QUIC\_STREAM\_UNI = 1 | 单向流，流只能由创建端发送数据，接收端只能接收。 |

### Rcp\_QuicStreamShutdown

```cpp
enum Rcp_QuicStreamShutdown
```

**描述**

quic流的关闭操作的类型。用于指定关闭流的读或写方向。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| RCP\_QUIC\_STREAM\_SHUTDOWN\_READ = 1 | 关闭流的读方向，不再接收数据。 |
| RCP\_QUIC\_STREAM\_SHUTDOWN\_WRITE = 2 | 关闭流的写方向，不再发送数据。 |

## 函数说明

### HMS\_Rcp\_CallNextRequestHandler()

```cpp
uint32_t HMS_Rcp_CallNextRequestHandler (Rcp_Request * request, const Rcp_RequestHandler * next, const Rcp_ResponseCallbackObject * responseCallback )
```

**描述**

在拦截器[Rcp\_Interceptor](_rcp___interceptor.md)的函数中可以调用下一个拦截器或defaultHandler。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 指向[Rcp\_Request](_rcp___request.md)的指针。 |
| next | 指向下一个异步处理器的指针[Rcp\_RequestHandler](remote-communication-overview.md#rcp_requesthandler)。 |
| responseCallback | 响应回调。指向[Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md)的指针。 |

**返回：**

uint32\_t。[401](errorcode-universal.md#section401-参数检查失败) - 参数错误 或 表示下一个异步处理器的返回值。

### HMS\_Rcp\_CallNextSyncRequestHandler()

```cpp
Rcp_Response* HMS_Rcp_CallNextSyncRequestHandler (Rcp_Request * request, const Rcp_SyncRequestHandler * next, uint32_t * errCode )
```

**描述**

在拦截器[Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)的函数中可以调用下一个拦截器或默认处理器。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 指向[Rcp\_Request](_rcp___request.md)的指针。 |
| next | 指向下一个同步处理器的指针[Rcp\_SyncRequestHandler](remote-communication-overview.md#rcp_syncrequesthandler)。 |
| errCode | 输出项。[401](errorcode-universal.md#section401-参数检查失败)：参数错误 或 表示下一个同步处理器的返回值。 |

**返回：**

Rcp\_Response\* 返回响应。

### HMS\_Rcp\_CancelRequest()

```cpp
uint32_t HMS_Rcp_CancelRequest (Rcp_Session * session, const Rcp_Request * request )
```

**描述**

取消一个请求。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| session | 需要取消请求的会话。指向[Rcp\_Session](remote-communication-overview.md#rcp_session)的指针。 |
| request | 需要取消的请求。指向要关闭的[Rcp\_Request](_rcp___request.md)的指针。 |

**返回：**

取消成功时返回0，权限不足时返回[201](errorcode-universal.md#section201-权限校验失败)，输入参数为空指针时返回[401](errorcode-universal.md#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](errorcode-remote-communication.md#section1007900993-会话已关闭)。

### HMS\_Rcp\_CancelSession()

```cpp
uint32_t HMS_Rcp_CancelSession (Rcp_Session * session)
```

**描述**

取消会话。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 描述 |
| --- | --- |
| session | 需要取消的会话。指向要关闭的[Rcp\_Session](remote-communication-overview.md#rcp_session)的指针。 |

**返回：**

取消成功时返回0，权限不足时返回[201](errorcode-universal.md#section201-权限校验失败)，输入参数为空指针时返回[401](errorcode-universal.md#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](errorcode-remote-communication.md#section1007900993-会话已关闭)。

### HMS\_Rcp\_CloseSession()

```cpp
uint32_t HMS_Rcp_CloseSession (Rcp_Session ** session)
```

**描述**

关闭会话。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| session | 需要关闭的会话。指向[Rcp\_Session](remote-communication-overview.md#rcp_session)指针的指针。 |

**返回：**

关闭成功时返回0，权限不足时返回[201](errorcode-universal.md#section201-权限校验失败)，输入参数为空指针时返回[401](errorcode-universal.md#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](errorcode-remote-communication.md#section1007900993-会话已关闭)。

### HMS\_Rcp\_CreateForm()

```cpp
Rcp_Form* HMS_Rcp_CreateForm (void)
```

**描述**

创建一个简单表单。

**起始版本：** 5.0.0(12)

**返回：**

Rcp\_Form\* 指向[Rcp\_Form](remote-communication-overview.md#rcp_form)的指针。

### HMS\_Rcp\_CreateHeaders()

```cpp
Rcp_Headers* HMS_Rcp_CreateHeaders (void)
```

**描述**

为请求或响应创建标头。

**起始版本：** 5.0.0(12)

**返回：**

Rcp\_Headers\* 创建的标头。指向[Rcp\_Headers](remote-communication-overview.md#rcp_headers)的指针。

### HMS\_Rcp\_CreateMultipartForm()

```cpp
Rcp_MultipartForm* HMS_Rcp_CreateMultipartForm (void)
```

**描述**

创建一个多部分表单。

**起始版本：** 5.0.0(12)

**返回：**

Rcp\_MultipartForm\* 返回创建的多部分表单，指向[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)的指针。

### HMS\_Rcp\_CreateRequest()

```cpp
Rcp_Request* HMS_Rcp_CreateRequest (const char * url)
```

**描述**

创建请求。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| url | 请求URL。 |

**返回：**

Rcp\_Request\* 返回创建的请求。指向[Rcp\_Request](_rcp___request.md)的指针。

### HMS\_Rcp\_CreateRequestCookies()

```cpp
Rcp_RequestCookies* HMS_Rcp_CreateRequestCookies (void)
```

**描述**

创建空的请求Cookie。

**起始版本：** 5.0.0(12)

**返回：**

Rcp\_RequestCookies\* 返回指向已创建的[Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies)的指针。

### HMS\_Rcp\_CreateSession()

```cpp
Rcp_Session* HMS_Rcp_CreateSession (const Rcp_SessionConfiguration * configuration, uint32_t * errCode )
```

**描述**

创建会话。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| configuration | 会话配置。 |
| errCode | 0：成功。  [401](errorcode-universal.md#section401-参数检查失败)：参数错误。  [201](errorcode-universal.md#section201-权限校验失败)：权限不足。  [1007900027](errorcode-remote-communication.md#section1007900027-内存不足)：内存不足。 |

**返回：**

Rcp\_Session\* 返回创建的会话。指向[Rcp\_Session](remote-communication-overview.md#rcp_session)的指针。

### HMS\_Rcp\_GetDefaultSession()

```cpp
uint32_t HMS_Rcp_GetDefaultSession (Rcp_Session ** session)
```

**描述**

获取默认会话。

**需要权限：** ohos.permission.INTERNET（如需使用[PathPreference](remote-communication-overview.md#rcp_pathpreference-1)的RCP\_PATH\_PREFERENCE\_CELLULAR模式，则额外需要ohos.permission.GET\_NETWORK\_INFO）

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 6.1.1(24)

**参数:**

| 名称 | 描述 |
| --- | --- |
| session | 默认会话出参。默认会话指针将被复制到[Rcp\_Session](remote-communication-overview.md#rcp_session)指针所指向的位置。 |

**返回：**

设置成功时返回0，权限不足时返回[201](errorcode-universal.md#section201-权限校验失败)，输入参数为空指针时返回[1007900401](errorcode-remote-communication.md#section1007900401-接口参数错误)，遇到内存问题时返回[1007900027](errorcode-remote-communication.md#section1007900027-内存不足)。

### HMS\_Rcp\_DestroyForm()

```cpp
void HMS_Rcp_DestroyForm (Rcp_Form * form)
```

**描述**

销毁一个简单表单。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| form | 要销毁的表格。指向[Rcp\_Form](remote-communication-overview.md#rcp_form)的指针。 |

### HMS\_Rcp\_DestroyHeaderEntries()

```cpp
void HMS_Rcp_DestroyHeaderEntries (Rcp_HeaderEntry * headerEntry)
```

**描述**

销毁[HMS\_Rcp\_GetHeaderEntries](remote-communication-overview.md#hms_rcp_getheaderentries)中获取的所有键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| headerEntry | 指向要销毁的[Rcp\_HeaderEntry](_rcp___header_entry.md)的指针。 |

### HMS\_Rcp\_DestroyHeaders()

```cpp
void HMS_Rcp_DestroyHeaders (Rcp_Headers * headers)
```

**描述**

销毁请求或响应的标头。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| headers | 指向要销毁的[Rcp\_Headers](remote-communication-overview.md#rcp_headers)的指针。 |

### HMS\_Rcp\_DestroyMultipartForm()

```cpp
void HMS_Rcp_DestroyMultipartForm (Rcp_MultipartForm * multipartForm)
```

**描述**

销毁一个多部分表单。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| multipartForm | 要销毁的多部分表单。指向[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)的指针。 |

### HMS\_Rcp\_DestroyRequest()

```cpp
void HMS_Rcp_DestroyRequest (Rcp_Request * request)
```

**描述**

销毁请求。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 指向要销毁的[Rcp\_Request](_rcp___request.md)的指针。 |

### HMS\_Rcp\_DestroyRequestCookieEntries()

```cpp
void HMS_Rcp_DestroyRequestCookieEntries (Rcp_RequestCookieEntry * cookieEntry)
```

**描述**

销毁从[HMS\_Rcp\_GetRequestCookieValue](remote-communication-overview.md#hms_rcp_getrequestcookievalue)获取的所有与请求Cookie相关的键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cookieEntry | 指向要销毁的[Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md)的指针。 |

### HMS\_Rcp\_DestroyRequestCookies()

```cpp
void HMS_Rcp_DestroyRequestCookies (Rcp_RequestCookies * cookies)
```

**描述**

销毁请求Cookie。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cookies | 指向要销毁的[Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies)的指针。 |

### HMS\_Rcp\_DestroyResponseCookieAttrEntries()

```cpp
void HMS_Rcp_DestroyResponseCookieAttrEntries (Rcp_CookieAttributeEntry * entries)
```

**描述**

销毁响应Cookie属性。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| entries | 指向要销毁的[Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md)的指针。 |

### HMS\_Rcp\_Fetch()

```cpp
uint32_t HMS_Rcp_Fetch (Rcp_Session * session, Rcp_Request * request, const Rcp_ResponseCallbackObject * responseCallback )
```

**描述**

发送异步请求并获取响应。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| session | 发起请求使用的会话。指向[Rcp\_Session](remote-communication-overview.md#rcp_session)的指针。 |
| request | 发送的请求。指向[Rcp\_Request](_rcp___request.md)的指针。 |
| responseCallback | 指向用户定义的响应回调函数的指针。详情请参见[Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md)。 |

**返回：**

执行成功时返回0，权限不足时返回[201](errorcode-universal.md#section201-权限校验失败)，输入参数为空指针时返回[401](errorcode-universal.md#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](errorcode-remote-communication.md#section1007900993-会话已关闭)。

**权限：**

ohos.permission.INTERNET（如需使用[PathPreference](remote-communication-overview.md#rcp_pathpreference-1)的RCP\_PATH\_PREFERENCE\_CELLULAR模式，则额外需要ohos.permission.GET\_NETWORK\_INFO）

### HMS\_Rcp\_FetchSync()

```cpp
Rcp_Response* HMS_Rcp_FetchSync (Rcp_Session * session, Rcp_Request * request, uint32_t * errCode )
```

**描述**

发送同步请求并获取响应。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| session | 发起请求使用的会话。指向[Rcp\_Session](remote-communication-overview.md#rcp_session)的指针。 |
| request | 发送的请求。指向[Rcp\_Request](_rcp___request.md)的指针。 |
| errCode | [out] 输出常见的错误代码。  0：成功。  [201](errorcode-universal.md#section201-权限校验失败)：权限不足。  [401](errorcode-universal.md#section401-参数检查失败)：参数错误。  [1007900001](errorcode-remote-communication.md#section1007900001-不支持的协议)：不支持的协议。  [1007900003](errorcode-remote-communication.md#section1007900003-url格式错误)：URL使用了错误/非法的格式或缺少URL。  [1007900005](errorcode-remote-communication.md#section1007900005-代理服务器域名解析失败)：无法解析代理名称。  [1007900006](errorcode-remote-communication.md#section1007900006-域名解析失败)：无法解析主机名。  [1007900007](errorcode-remote-communication.md#section1007900007-无法连接到服务器)：无法连接到服务器。  [1007900008](errorcode-remote-communication.md#section1007900008-服务器返回非法数据)：异常的服务器回复。  [1007900009](errorcode-remote-communication.md#section1007900009-拒绝对远程资源的访问)：对远程资源的访问被拒绝。  [1007900016](errorcode-remote-communication.md#section1007900016-http2帧层错误)：HTTP2框架层中的错误。  [1007900018](errorcode-remote-communication.md#section1007900018-服务器返回数据不完整)：已传输部分文件。  [1007900025](errorcode-remote-communication.md#section1007900025-上传失败)：上载失败。  [1007900026](errorcode-remote-communication.md#section1007900026-从文件应用程序中打开读取本地数据失败)：无法从文件/应用程序中打开/读取本地数据。  [1007900027](errorcode-remote-communication.md#section1007900027-内存不足)：内存不足。  [1007900028](errorcode-remote-communication.md#section1007900028-操作超时)：已达到超时。  [1007900047](errorcode-remote-communication.md#section1007900047-重定向次数达到最大值)：重定向数达到最大数量。  [1007900052](errorcode-remote-communication.md#section1007900052-服务器没有返回内容)：服务器没有返回任何内容（没有标头，没有数据）。  [1007900055](errorcode-remote-communication.md#section1007900055-发送网络数据失败)：向对等方发送数据失败。  [1007900056](errorcode-remote-communication.md#section1007900056-接收网络数据失败)：从对等方接收数据时失败。  [1007900058](errorcode-remote-communication.md#section1007900058-本地ssl证书错误)：本地SSL证书有问题。  [1007900059](errorcode-remote-communication.md#section1007900059-无法使用指定的密码)：无法使用指定的SSL密钥。  [1007900060](errorcode-remote-communication.md#section1007900060-远程服务器ssl证书或ssh秘钥不正确)：SSL对等证书或SSH远程密钥不正常。  [1007900061](errorcode-remote-communication.md#section1007900061-无法识别或错误的http编码格式)：无法识别或错误的HTTP内容或传输编码。  [1007900063](errorcode-remote-communication.md#section1007900063-超出最大文件大小)：超过了最大文件大小。  [1007900070](errorcode-remote-communication.md#section1007900070-服务器磁盘空间不足)：磁盘已满或分配超出。  [1007900073](errorcode-remote-communication.md#section1007900073-服务器返回文件已存在)：远程文件已存在。  [1007900077](errorcode-remote-communication.md#section1007900077-ssl-ca证书不存在或没有访问权限)：SSL CA证书有问题 (路径？ 访问权限?)。  [1007900078](errorcode-remote-communication.md#section1007900078-url请求的文件不存在)：找不到远程文件。  [1007900992](errorcode-remote-communication.md#section1007900992-请求已被取消)：请求已取消。  [1007900993](errorcode-remote-communication.md#section1007900993-会话已关闭)：会话已关闭或无效。  [1007900094](errorcode-remote-communication.md#section1007900094-身份校验失败)：身份验证函数返回了错误。  [1007900201](errorcode-remote-communication.md#section1007900201-禁止明文传输)：禁止明文传输。从6.1.0(23)起新增支持此错误码。  [1007900995](errorcode-remote-communication.md#section1007900995-获取系统代理失败)：获取系统代理失败。  [1007900996](errorcode-remote-communication.md#section1007900996-代理类型不支持)：代理类型不受支持。  [1007900997](errorcode-remote-communication.md#section1007900997-无效的内容类型)：无效的内容类型。  [1007900998](errorcode-remote-communication.md#section1007900998-所请求的方法不被支持)：方法不受支持。  [1007900999](errorcode-remote-communication.md#section1007900999-内部错误)：内部错误。  Others：1007900000 + CURL\_ERROR\_CODE。更多常见的错误码，请参见[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)。 |

**返回：**

Rcp\_Response\* 返回的响应。指向[Rcp\_Response](_rcp___response.md)的指针。

**权限：**

ohos.permission.INTERNET（如需使用[PathPreference](remote-communication-overview.md#rcp_pathpreference-1)的RCP\_PATH\_PREFERENCE\_CELLULAR模式，则额外需要ohos.permission.GET\_NETWORK\_INFO）

### HMS\_Rcp\_GetFormValue()

```cpp
Rcp_FormFieldValue* HMS_Rcp_GetFormValue (Rcp_Form * form, const char * key )
```

**描述**

通过键获取一个简单表单的对应值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| form | 指向[Rcp\_Form](remote-communication-overview.md#rcp_form)的指针。 |
| key | 键。 |

**返回：**

Rcp\_FormFieldValue\* 值。指向{@Rcp\_FormFieldValue}的指针。

### HMS\_Rcp\_GetHeaderEntries()

```cpp
Rcp_HeaderEntry* HMS_Rcp_GetHeaderEntries (Rcp_Headers * headers)
```

**描述**

获取请求或响应头的所有键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| headers | 指向要获取所有键值对的[Rcp\_Headers](remote-communication-overview.md#rcp_headers)的指针。 |

**返回：**

Rcp\_HeaderEntry\* 指向所有获取到的键值对[Rcp\_HeaderEntry](_rcp___header_entry.md)。

### HMS\_Rcp\_GetHeaderValue()

```cpp
Rcp_HeaderValue* HMS_Rcp_GetHeaderValue (Rcp_Headers * headers, const char * name)
```

**描述**

通过键获取请求或响应头的值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| headers | 指向要获取值的[Rcp\_Headers](remote-communication-overview.md#rcp_headers)的指针。 |
| name | 键。 |

**返回：**

Rcp\_HeaderValue\* 指向获得的[Rcp\_HeaderValue](_rcp___header_value.md)的指针。

### HMS\_Rcp\_GetMultipartFormValue()

```cpp
Rcp_MultipartFormFieldValue* HMS_Rcp_GetMultipartFormValue (Rcp_MultipartForm * multipartForm, const char * key)
```

**描述**

通过键获取多部分表单的值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| multipartForm | 需要获取值的多部分表单。指向[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)的指针。 |
| key | 键。 |

**返回：**

Rcp\_MultipartFormFieldValue\* 多部分表单的值。指向[Rcp\_MultipartFormFieldValue](_rcp___multipart_form_field_value.md)的指针。

### HMS\_Rcp\_SetFormOrder()

```cpp
uint32_t HMS_Rcp_SetFormOrder (Rcp_Form * form, Rcp_FormOrder order)
```

**描述**

设置Form表单的键值对发送顺序。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| form | 需要设置的表单。指向[Rcp\_Form](remote-communication-overview.md#rcp_form)的指针。 |
| order | 指定的keys顺序。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[1007900401](errorcode-remote-communication.md#section1007900401-接口参数错误)，内存问题返回[1007900027](errorcode-remote-communication.md#section1007900027-内存不足)。

### HMS\_Rcp\_SetMultipartFormOrder()

```cpp
uint32_t HMS_Rcp_SetMultipartFormOrder (Rcp_MultipartForm * multipartForm, Rcp_FormOrder order)
```

**描述**

设置MultipartForm表单的键值对发送顺序。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| multipartForm | 需要设置的表单。指向[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)的指针。 |
| order | 指定的keys顺序。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[1007900401](errorcode-remote-communication.md#section1007900401-接口参数错误)，内存问题返回[1007900027](errorcode-remote-communication.md#section1007900027-内存不足)。

### HMS\_Rcp\_GetRequestCookieEntries()

```cpp
Rcp_RequestCookieEntry* HMS_Rcp_GetRequestCookieEntries (Rcp_RequestCookies * cookies)
```

**描述**

获取请求Cookie中的所有键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cookies | 需要获取所有键值对的请求Cookie。指向[Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies)的指针。 |

**返回：**

Rcp\_RequestCookieEntry\* 返回请求Cookie中的所有键值对。指向[Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md)的指针。

### HMS\_Rcp\_GetRequestCookieValue()

```cpp
char* HMS_Rcp_GetRequestCookieValue (Rcp_RequestCookies * cookies, const char * name)
```

**描述**

通过名称获取请求Cookie的值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cookies | 需要获取值的请求Cookie。指向[Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies)的指针。 |
| name | 键。 |

**返回：**

char\* 返回请求Cookie的值。

### HMS\_Rcp\_GetResponseCookieAttrEntries()

```cpp
Rcp_CookieAttributeEntry* HMS_Rcp_GetResponseCookieAttrEntries (Rcp_CookieAttributes * cookieAttributes)
```

**描述**

在[Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes)中获取所有响应Cookie属性。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cookieAttributes | 指向要获取所有Cookie属性的[Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes)的指针。 |

**返回：**

[Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md) \* 响应的Cookie属性列表。

### HMS\_Rcp\_GetResponseCookieAttrValue()

```cpp
const char* HMS_Rcp_GetResponseCookieAttrValue (Rcp_CookieAttributes * cookieAttributes, const char * name)
```

**描述**

通过名称获取Cookie属性的值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cookieAttributes | 指向要获取值的[Rcp\_CookieAttributes](remote-communication-overview.md#rcp_cookieattributes)的指针。 |
| name | 键。 |

**返回：**

char\* Cookie属性中的值。

### HMS\_Rcp\_GetSessionConfiguration()

```cpp
const Rcp_SessionConfiguration* HMS_Rcp_GetSessionConfiguration (Rcp_Session * session)
```

**描述**

获取会话配置。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| session | 需要获取会话配置的会话。指向[Rcp\_Session](remote-communication-overview.md#rcp_session)的指针。 |

**返回：**

Rcp\_SessionConfiguration\* 返回的会话配置。指向[Rcp\_SessionConfiguration](_rcp___session_configuration.md)的指针。

### HMS\_Rcp\_GetSessionId()

```cpp
const char* HMS_Rcp_GetSessionId (Rcp_Session * session)
```

**描述**

获取会话ID。

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| session | 需要获取会话ID的会话。指向[Rcp\_Session](remote-communication-overview.md#rcp_session)的指针。 |

**返回：**

char\* 返回的会话ID。

### HMS\_Rcp\_SetFormValue()

```cpp
uint32_t HMS_Rcp_SetFormValue (Rcp_Form * form, const char * key, const Rcp_FormFieldValue * value)
```

**描述**

设置简单表单的键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| form | 需要设置键值对的表单。指向[Rcp\_Form](remote-communication-overview.md#rcp_form)的指针。 |
| key | 键。 |
| value | 值。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[401](errorcode-universal.md#section401-参数检查失败)，内存问题返回[1007900027](errorcode-remote-communication.md#section1007900027-内存不足)。

### HMS\_Rcp\_SetHeaderValue()

```cpp
uint32_t HMS_Rcp_SetHeaderValue (Rcp_Headers * headers, const char * name, const char * value)
```

**描述**

设置请求或响应头的键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| headers | 指向要设置的[Rcp\_Headers](remote-communication-overview.md#rcp_headers)的指针。 |
| name | 键。 |
| value | 值。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[401](errorcode-universal.md#section401-参数检查失败)，内存问题返回[1007900027](errorcode-remote-communication.md#section1007900027-内存不足)。

### HMS\_Rcp\_SetMultipartFormValue()

```cpp
uint32_t HMS_Rcp_SetMultipartFormValue (Rcp_MultipartForm * multipartForm, const char * key, const Rcp_MultipartFormFieldValue * value)
```

**描述**

设置多部分表单的键值对。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| multipartForm | 需要设置的多部分表单。指向[Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform)的指针。 |
| key | 键。 |
| value | 值。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[401](errorcode-universal.md#section401-参数检查失败)，内存问题返回[1007900027](errorcode-remote-communication.md#section1007900027-内存不足)。

### HMS\_Rcp\_SetRequestCookieValue()

```cpp
uint32_t HMS_Rcp_SetRequestCookieValue (Rcp_RequestCookies * cookies, const char * name, const char * value)
```

**描述**

设置请求Cookie。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| cookies | 需要设置的请求Cookie。指向[Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies)的指针。 |
| name | 键。 |
| value | 值。 |

**返回：**

设置成功返回0，入参有空指针或者size大小为0时返回[401](errorcode-universal.md#section401-参数检查失败)，内存问题返回[1007900027](errorcode-remote-communication.md#section1007900027-内存不足)。

### HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback()

```cpp
uint32_t HMS_Rcp_SetRequestOnBinaryDataRecvCallback (Rcp_Request * request, Rcp_OnBinaryReceiveCallback onBinaryReceiveCallback)
```

**描述**

为请求设置流式接收二进制数据的回调函数。该回调函数与[Rcp\_Configuration](_rcp___configuration.md)中配置的[Rcp\_OnDataReceiveCallback](remote-communication-overview.md#rcp_ondatareceivecallback)功能一致。设置后将替换在[Rcp\_Configuration](_rcp___configuration.md)中配置的[Rcp\_OnDataReceiveCallback](remote-communication-overview.md#rcp_ondatareceivecallback)。

**起始版本：** 5.0.1(13)

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 需要设置二进制数据回调的请求。指向[Rcp\_Request](remote-communication-overview.md#rcp_request)的指针。 |
| onBinaryReceiveCallback | 需要设置的二进制数据接收回调函数。 |

**返回：**

设置成功返回0，参数错误时返回[401](errorcode-universal.md#section401-参数检查失败)。

### HMS\_Rcp\_SetRequestConnectOnly()

```cpp
uint32_t HMS_Rcp_SetRequestConnectOnly (Rcp_Request * request, bool connectOnly)
```

**描述**

设置请求仅用于建立连接，而不进行数据传输。

**起始版本：** 6.1.1(24)

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 需要仅用于建立连接的请求。指向[Rcp\_Request](remote-communication-overview.md#rcp_request)的指针。 |
| connectOnly | 此选项用于确定请求是否仅用于建立连接。如果设置为true，则表示本次请求仅用于建立连接；如果设置为false，则表示本次请求可以传输数据。默认值为false。 |

**返回：**

设置成功时返回0，输入参数为空指针时返回[1007900401](errorcode-remote-communication.md#section1007900401-接口参数错误)。

### HMS\_Rcp\_SetRequestOnStatusCodeReceiveCallback()

```cpp
uint32_t HMS_Rcp_SetRequestOnStatusCodeReceiveCallback (Rcp_Request * request, Rcp_OnStatusCodeReceiveCallback onStatusCodeReceiveCallback)
```

**描述**

为请求设置响应状态码回调函数。在请求收到对端返回的响应码时触发。不可通过重新设置[Rcp\_OnStatusCodeReceiveCallbackFunc](remote-communication-overview.md#rcp_onstatuscodereceivecallbackfunc)为NULL实现取消监听。

**起始版本：** 6.0.1(21)

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 需要设置响应状态码回调的请求。指向[Rcp\_Request](remote-communication-overview.md#rcp_request)的指针。 |
| onStatusCodeReceiveCallback | 需要设置的响应状态码接收回调函数。 |

**返回：**

设置成功返回0，参数错误时返回[401](errorcode-universal.md#section401-参数检查失败)。

### HMS\_Rcp\_SetRequestGetDataCallback()

```cpp
uint32_t HMS_Rcp_SetRequestGetDataCallback (Rcp_Request * request, Rcp_OnGetDataCallback  getDataCallback)
```

**描述**

设置获取数据的回调函数。不可通过重新设置[Rcp\_GetDataCallbackFunc](remote-communication-overview.md#rcp_getdatacallbackfunc)为NULL实现取消监听。调用此函数设置非空的[Rcp\_GetDataCallbackFunc](remote-communication-overview.md#rcp_getdatacallbackfunc)后，[Rcp\_Request](remote-communication-overview.md#rcp_request)的[content](_rcp___request.md#content)失效。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 需要设置响应回调的请求。指向[Rcp\_Request](remote-communication-overview.md#rcp_request)的指针。 |
| getDataCallback | 需要设置获取数据的回调函数。 |

**返回：**

设置成功时返回0，输入request参数为空指针时返回[1007900401](errorcode-remote-communication.md#section1007900401-接口参数错误)。

### HMS\_Rcp\_QuicConnSetOpt()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicConnSetOpt (Rcp_QuicConn *conn, Rcp_QuicConnOpt opt, const void *optVal, uint32_t optLen)
```

**描述**

设置quic连接选项。用于设置连接的各种参数和回调函数。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| opt | quic连接选项类型，可配置[Rcp\_QuicConnOpt](remote-communication-overview.md#rcp_quicconnopt)类型参数。 |
| optVal | quic连接选项的值。 |
| optLen | quic连接选项的长度。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic连接选项配置结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS为配置quic连接选项成功，其余返回值均为配置失败。

### HMS\_Rcp\_QuicConnGetInfo()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicConnGetInfo (Rcp_QuicConn *conn, Rcp_QuicConnInfo info, void *infoVal, uint32_t *infoLen)
```

**描述**

获取quic连接信息。用于建立quic连接成功后，获取相关quic连接信息。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| info | quic连接信息类型，可获得[Rcp\_QuicConnInfo](remote-communication-overview.md#rcp_quicconninfo)相关参数。 |
| infoVal | quic连接信息的值。 |
| infoLen | quic连接信息的长度。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic连接信息获取结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示获取quic连接相关参数成功，其余返回值均为获取失败。

### HMS\_Rcp\_QuicStreamSetOpt()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicStreamSetOpt (Rcp_QuicConn *conn, uint64_t streamId, Rcp_QuicStreamOpt opt, const void *optVal, uint32_t optLen)
```

**描述**

设置quic连接中流的参数。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| opt | quic流选项类型，可配置[Rcp\_QuicStreamOpt](remote-communication-overview.md#rcp_quicstreamopt)类型相关选项。 |
| optVal | quic流选项的值。 |
| optLen | quic流选项的长度。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic流选项配置结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示配置quic相关选项成功，其余返回值均为配置失败。

### HMS\_Rcp\_QuicStreamGetInfo()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicStreamGetInfo (Rcp_QuicConn *conn, uint64_t streamId, Rcp_QuicStreamInfo info, void *infoVal, uint32_t *infoLen)
```

**描述**

获取quic连接中streamId对应流的信息。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| info | quic流信息类型，可获取[Rcp\_QuicStreamInfo](remote-communication-overview.md#rcp_quicstreaminfo)类型相关信息。 |
| infoVal | quic流信息的值。 |
| infoLen | quic流信息的长度。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic流信息获取结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示获取quic流相关参数成功，其余返回值均为获取失败。

### HMS\_Rcp\_QuicCreateSession()

```cpp
Rcp_QuicSession *HMS_Rcp_QuicCreateSession ()
```

**描述**

创建quic会话对象。一个quic会话中可以管理多个quic连接。

**起始版本：** 26.0.0

**返回：**

[Rcp\_QuicSession](remote-communication-overview.md#rcp_quicsession)\*: quic会话对象指针，失败返回NULL。

### HMS\_Rcp\_QuicDestroySession()

```cpp
void HMS_Rcp_QuicDestroySession (Rcp_QuicSession *session)
```

**描述**

销毁quic会话对象。释放quic会话资源。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| session | quic会话对象。 |

### HMS\_Rcp\_QuicConnCreate()

```cpp
Rcp_QuicConn *HMS_Rcp_QuicConnCreate (char *alpn, void *userObject)
```

**描述**

创建quic连接对象。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| alpn | 应用层协议协商（ALPN）字符串。 |
| userObject | 用户定义的对象。 |

**返回：**

[Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn)\*: quic连接对象指针，失败返回NULL。

### HMS\_Rcp\_QuicConnConnect()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicConnConnect (Rcp_QuicSession *session, Rcp_QuicConn *conn, const char *serverName, uint16_t port)
```

**描述**

发起quic连接握手。握手结果通过连接回调通知。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| session | quic会话对象。 |
| conn | quic连接对象。 |
| serverName | 服务器名称（域名或IP地址）。 |
| port | 服务器端口号。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic连接发起结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示quic连接发起成功，其余返回值均为发起失败。

**权限：**

ohos.permission.INTERNET

### HMS\_Rcp\_QuicConnDestroy()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicConnDestroy (Rcp_QuicConn *conn)
```

**描述**

销毁QUIC连接，完成后触发[Rcp\_QuicConnectionOnClosed](remote-communication-overview.md#rcp_quicconnectiononclosed)事件。请勿对同一个[Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn)实例重复执行此操作。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic连接对象销毁结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示quic连接对象销毁成功，其余返回值均为销毁失败。

### HMS\_Rcp\_QuicConnStreamOpen()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamOpen (Rcp_QuicConn *conn, Rcp_QuicStreamDirection direction, uint64_t *streamId, void *userObject)
```

**描述**

在quic连接中打开一个quic流。quic连接建立成功后才能打开quic流。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| direction | quic流方向，配置quic方向[Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection)枚举类型。 |
| streamId | 创建的quic流ID指针。 |
| userObject | 流回调的用户对象。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic流创建结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示quic流创建成功，其余返回值均为创建失败。

**权限：**

ohos.permission.INTERNET

### HMS\_Rcp\_QuicConnStreamSend()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamSend (Rcp_QuicConn *conn, uint64_t streamId, const Rcp_QuicIoVec *ioVec, uint32_t ioVecCount, bool fin)
```

**描述**

通过quic流发送数据。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| ioVec | 发送的内容数据向量数组。 |
| ioVecCount | 发送的内容数据向量数量。 |
| fin | true表示发送内容是最后一段数据，false表示发送的内容不是最后一段数据。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic流发送数据结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示quic流发送数据成功，其余返回值均为发送失败。

**权限：**

ohos.permission.INTERNET

### HMS\_Rcp\_QuicConnStreamWantRead()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamWantRead (Rcp_QuicConn *conn, uint64_t streamId)
```

**描述**

触发quic流数据读取回调。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic流数据读取回调开启结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示quic流数据读取回调开启成功，其余返回值均为开启失败。

### HMS\_Rcp\_QuicConnStreamReset()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamReset (Rcp_QuicConn *conn, uint64_t streamId, uint64_t appErr)
```

**描述**

重置quic流。立即终止流，丢弃所有未发送和已接收的数据。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| appErr | 应用错误码。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic流重置结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示quic流重置成功，其余返回值均为重置失败。

**权限：**

ohos.permission.INTERNET

### HMS\_Rcp\_QuicConnStreamShutdown()

```cpp
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamShutdown (Rcp_QuicConn *conn, uint64_t streamId, Rcp_QuicStreamShutdown flag, uint64_t appErr)
```

**描述**

关闭连接中streamId对应流的读或写。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| flag | quic流关闭标志，可选[Rcp\_QuicStreamShutdown](remote-communication-overview.md#rcp_quicstreamshutdown)类型。 |
| appErr | 应用错误码。 |

**返回：**

[Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode): quic流关闭结果，RCP\_QUIC\_ERROR\_CODE\_SUCCESS表示quic流关闭成功，其余返回值均为关闭失败。

**权限：**

ohos.permission.INTERNET

### HMS\_Rcp\_QuicStreamGetDirection()

```cpp
Rcp_QuicStreamDirection HMS_Rcp_QuicStreamGetDirection (uint64_t streamId)
```

**描述**

获取quic流的方向类型。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| streamId | quic流ID。 |

**返回：**

[Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection): quic流的方向，RCP\_QUIC\_STREAM\_BIDI表示双向流，RCP\_QUIC\_STREAM\_UNI表示单向流。

### HMS\_Rcp\_QuicFreeSlist()

```cpp
void HMS_Rcp_QuicFreeSlist (Rcp_QuicSlist *list)
```

**描述**

释放[Rcp\_QuicSlist](_rcp___quic_slist.md)链表，释放链表中的所有节点和数据。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| list | [Rcp\_QuicSlist](_rcp___quic_slist.md)链表指针。 |
