---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisespacekit-6003
title: Enterprise Space Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Enterprise Space Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:17+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5ad27bde3dc0ec8825d2d9f2dd14455af60b91993bdb0f931e3d2d5c5cd970a2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace spaceManager  差异内容：declare namespace spaceManager | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：interface CreateWorkspaceParams  差异内容：interface CreateWorkspaceParams | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：CreateWorkspaceParams；  API声明：shortName: string;  差异内容：shortName: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：interface WorkspaceDomainInfo  差异内容：interface WorkspaceDomainInfo | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceDomainInfo；  API声明：domain: string;  差异内容：domain: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceDomainInfo；  API声明：workspaceName: string;  差异内容：workspaceName: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceDomainInfo；  API声明：accountId?: string;  差异内容：accountId?: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceDomainInfo；  API声明：isAuthenticated?: boolean;  差异内容：isAuthenticated?: boolean; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceDomainInfo；  API声明：serverConfigId?: string;  差异内容：serverConfigId?: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：interface WorkspaceInfo  差异内容：interface WorkspaceInfo | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：workspaceId: number;  差异内容：workspaceId: number; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：localName: string;  差异内容：localName: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：shortName?: string;  差异内容：shortName?: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：isUnlocked: boolean;  差异内容：isUnlocked: boolean; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：photo: string;  差异内容：photo: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：createTime: number;  差异内容：createTime: number; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：lastLoginTime: number;  差异内容：lastLoginTime: number; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：serialNumber: number;  差异内容：serialNumber: number; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：isActivated: boolean;  差异内容：isActivated: boolean; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：isCreateCompleted: boolean;  差异内容：isCreateCompleted: boolean; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：isAllowedToBeDeleted: boolean;  差异内容：isAllowedToBeDeleted: boolean; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceInfo；  API声明：domainInfo: WorkspaceDomainInfo;  差异内容：domainInfo: WorkspaceDomainInfo; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：interface EventData  差异内容：interface EventData | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：EventData；  API声明：event: EventType;  差异内容：event: EventType; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：EventData；  API声明：currentWorkspaceId?: number;  差异内容：currentWorkspaceId?: number; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：enum WorkspaceType  差异内容：enum WorkspaceType | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：WorkspaceType；  API声明：ADMIN = 0  差异内容：ADMIN = 0 | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：enum QueryType  差异内容：enum QueryType | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：QueryType；  API声明：ALL = 0  差异内容：ALL = 0 | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：QueryType；  API声明：NON\_DELETABLE = 1  差异内容：NON\_DELETABLE = 1 | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：enum EventType  差异内容：enum EventType | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：EventType；  API声明：EVENT\_WORKSPACE\_SWITCHED = 0  差异内容：EVENT\_WORKSPACE\_SWITCHED = 0 | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function createWorkspace(localName: string, workspaceType: WorkspaceType, params?: CreateWorkspaceParams): Promise<WorkspaceInfo>;  差异内容：function createWorkspace(localName: string, workspaceType: WorkspaceType, params?: CreateWorkspaceParams): Promise<WorkspaceInfo>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function enableWorkspace(enable: boolean): Promise<void>;  差异内容：function enableWorkspace(enable: boolean): Promise<void>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function queryWorkspace(queryFlag: QueryType): Promise<WorkspaceInfo[]>;  差异内容：function queryWorkspace(queryFlag: QueryType): Promise<WorkspaceInfo[]>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function removeWorkspace(workspaceId: number): Promise<void>;  差异内容：function removeWorkspace(workspaceId: number): Promise<void>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function setWorkspaceInfo(workspaceId: number, domainInfo: WorkspaceDomainInfo): Promise<void>;  差异内容：function setWorkspaceInfo(workspaceId: number, domainInfo: WorkspaceDomainInfo): Promise<void>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function setWorkspaceProfilePhoto(workspaceId: number, photo: string): Promise<void>;  差异内容：function setWorkspaceProfilePhoto(workspaceId: number, photo: string): Promise<void>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function subscribeEvent(eventId: EventType[], callback: AsyncCallback<EventData>): number;  差异内容：function subscribeEvent(eventId: EventType[], callback: AsyncCallback<EventData>): number; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager；  API声明：function unsubscribeEvent(subscribeId: number): void;  差异内容：function unsubscribeEvent(subscribeId: number): void; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：fileTransfer；  API声明：function policyPush(policyContext: string): void;  差异内容：function policyPush(policyContext: string): void; | api/@hms.enterpriseSpaceService.fileTransfer.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.enterpriseSpaceService.spaceManager.d.ts  差异内容：EnterpriseSpaceKit | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
