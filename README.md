# Hi, I'm Abhimanyu Saharan

I build developer tools, web applications, and the infrastructure that runs them. My work spans Kubernetes and GitOps, Python and TypeScript, self-hosted systems, and AI agents with access to real tools.

I like working across the whole system: the application, its deployment, the automation around it, and what happens when something breaks. That shows up in both the products I build and the ARM64 Raspberry Pi homelab where I run and experiment with services.

I share implementations, debugging notes, and lessons from that work on [my blog](https://blog.abhimanyu-saharan.com). Recent writing covers homelab networking, Kubernetes, cluster cooling, and CI/CD.

## What I'm building

| Project | What it's for |
| --- | --- |
| [DevFeed](https://devfeed.tech) · [Code](https://github.com/abhi1693/devfeed.tech) | Developer news, tutorials, and releases in one reading feed, with public MCP access for discovering content through agents. |
| [Wardn AI](https://github.com/abhi1693/wardn-ai) | A control plane for AI agents and MCP tools: approved servers, scoped credentials, human approvals, execution, and audit trails. |
| [Wardn Hub](https://hub.wardnai.dev/) · [Code](https://github.com/abhi1693/wardn-hub) | A catalog for discovering and evaluating agent skills, with scanning and validation tooling. |
| [ShipyardHQ](https://shipyardhq.dev) · [Code](https://github.com/abhi1693/shipyardhq) | Product discovery beyond launch day, with directories, rankings, and launch analytics for apps, SaaS, AI tools, and APIs. |
| [GetEnvelope](https://github.com/abhi1693/getenvelope) | An early-stage project and service inbox with agent assistance; currently an application scaffold. |
| [Open-LLM Router](https://github.com/abhi1693/open-llm-router) | An OpenAI-compatible gateway for routing requests across model providers, with failover, logging, and metrics. |
| [NetBox SSOT](https://github.com/abhi1693/netbox-ssot) | Compare, review, and synchronize infrastructure data between NetBox instances. |
| [Firefly Importer](https://github.com/abhi1693/firefly-importer) | Bank, credit card, and mutual fund statement parsers and import workflows for Firefly III, with reconciliation checks. |

## Infrastructure and everyday automation

My [homelab](https://github.com/abhi1693/homelab) brings together ARM64 Raspberry Pis, Ansible, K3s, Rancher Fleet, custom container images, and development environments. It's where application work meets networking, storage, observability, backups, and recovery.

Alongside it, I maintain:

- [Shared GitHub Actions](https://github.com/abhi1693/actions) for reusable CI, container builds, scanning, and release automation.
- [Harbor ARM64 builds](https://github.com/abhi1693/harbor) to build and publish upstream Harbor components for ARM64.
- [Home Assistant configuration](https://github.com/abhi1693/home-assistant) with GitOps, family dashboards, custom integrations, and reproducible setup.
- [HA Sensors Gateway](https://github.com/abhi1693/ha-sensors-gateway) for narrowly scoped Home Assistant sensor and location webhooks.
- [qBittorrent Smart Queues](https://github.com/abhi1693/qbittorrent-smart-queues) for queue, quota, and health control.
- [Kubernetes Recommendation Engine](https://github.com/abhi1693/k8s-recommendation-engine) and [Music Assistant / YouTube Music tooling](https://github.com/abhi1693/music-assistant-yt-music).

## More projects

<details>
<summary>Experiments, libraries, earlier work, and supporting repositories</summary>

### Agents and workflow experiments

- [Jarvis](https://github.com/abhi1693/jarvis) — a local-first multimodal agent scaffold with persistent memory.
- [Agent Ops](https://github.com/abhi1693/agent-ops) — an application and workflow platform experiment.

### Libraries and integrations

- [Python Packer](https://github.com/abhi1693/python-packer) — a Python interface for Packer.
- [setup-browser](https://github.com/abhi1693/setup-browser) and [setup-megacmd](https://github.com/abhi1693/setup-megacmd) — GitHub Actions setup tools.
- [WPimporter](https://github.com/abhi1693/oc-wpimporter) — move WordPress posts into October CMS.

### Earlier PHP and Yii2 work

[User authentication](https://github.com/abhi1693/yii2-user) ·
[RBAC](https://github.com/abhi1693/yii2-rbac) ·
[System information](https://github.com/abhi1693/yii2-system-info) ·
[SMS](https://github.com/abhi1693/yii2-sms) ·
[Installer](https://github.com/abhi1693/yii2-installer) ·
[Enum helper](https://github.com/abhi1693/yii2-enum) ·
[Database configuration](https://github.com/abhi1693/yii2-config) ·
[Blog startup kit](https://github.com/abhi1693/yii2-app-blog-startup-kit) ·
[Advanced startup kit](https://github.com/abhi1693/yii2-app-advanced-startup-kit) ·
[Desk CMS](https://github.com/abhi1693/desk) ·
[Tux Tips user plugin](https://github.com/abhi1693/user) ·
[Tux Tips forum plugin](https://github.com/abhi1693/forum)

### Containers, configuration, and learning

[nginx-proxy](https://github.com/abhi1693/nginx-proxy) ·
[docker-barman](https://github.com/abhi1693/docker-barman) ·
[Docker demo](https://github.com/abhi1693/docker-demo-image) ·
[Dotfiles](https://github.com/abhi1693/dotfiles) ·
[Coder dotfiles](https://github.com/abhi1693/dotfiles-coder) ·
[Katacoda scenarios](https://github.com/abhi1693/katacoda-scenarios) ·
[GitHub Slideshow](https://github.com/abhi1693/github-slideshow)

### Sites and supporting repositories

[Personal blog](https://github.com/abhi1693/personal-blog) ·
[Blog discussions](https://github.com/abhi1693/personal-blog-discussions) ·
[Portfolio](https://github.com/abhi1693/portfolio) ·
[Wardn website](https://github.com/abhi1693/wardn-ai-website) ·
[This profile and its generator](https://github.com/abhi1693/abhi1693)

</details>

## On DevFeed

[![DevFeed card](https://devfeed.tech/api/v1/users/asaharan/card.svg)](https://devfeed.tech/users/asaharan)

## Reading from DevFeed 📖

A fresh reading list from [DevFeed](https://devfeed.tech): five recent articles on software, tools, and the systems behind them.

### 1. [How Agent Anomaly Detection scores on benchmarks we didn't write](<https://developers.googleblog.com/how-agent-anomaly-detection-scores-on-benchmarks-we-didnt-write/>)

**Google Developers Blog** · News

In five public benchmarks totaling 1,774 sessions, Agent Anomaly Detection (AAD) flagged 87% of harmful instructions that agents carried out, analyzing traces and logs asynchronously without adding runtime latency.

[Read article →](<https://developers.googleblog.com/how-agent-anomaly-detection-scores-on-benchmarks-we-didnt-write/>)

---

### 2. [How attackers turned a Teams meeting booking into a device code phishing trap](<https://www.helpnetsecurity.com/2026/11/13/microsoft-teams-device-code-phishing/>)

**Help Net Security** · News · Nov 13, 2026

A fake Teams meeting scheduler turned the meeting “booking reference” into a Microsoft device code, leading an employee to approve the attacker’s sign-in and grant access tokens.

[Read article →](<https://www.helpnetsecurity.com/2026/11/13/microsoft-teams-device-code-phishing/>)

---

### 3. [Best Tools for AI Concierge for Employee Support Automation in 2026](<https://www.lyzr.ai/blog/best-tools-for-ai-concierge-for-employee-support-automation/>)

**Lyzr.ai** · Comparison · Nov 13, 2026

An employee support concierge is most useful when it can retrieve information and execute requests across connected systems, with access controls and escalation for complex cases.

[Read article →](<https://www.lyzr.ai/blog/best-tools-for-ai-concierge-for-employee-support-automation/>)

---

### 4. [A Desktop OS for the ESP32-P4](<https://hackaday.com/2026/11/12/a-desktop-os-for-the-esp32-p4/>)

**Hackaday** · News · Nov 13, 2026

BMDS is a desktop-style OS for the ESP32-P4, targeting an Olimex board. It uses FreeRTOS as its kernel and adds a minimally intrusive, single-user environment described as DOS-like. It runs ELF binaries, offers some POSIX compliance, and includes a BusyBox port.

[Read article →](<https://hackaday.com/2026/11/12/a-desktop-os-for-the-esp32-p4/>)

---

### 5. [Your pinned MCP server may not be as pinned as you think](<https://www.helpnetsecurity.com/2026/11/13/corelight-mcp-server-supply-chain/>)

**Help Net Security** · News · Nov 13, 2026

A fixed MCP server release did not keep its dependencies fixed: over five weeks, an administrator’s workstation built 15 dependency sets without configuration changes, and 23 of 69 packages changed versions.

[Read article →](<https://www.helpnetsecurity.com/2026/11/13/corelight-mcp-server-supply-chain/>)


---

Updated 2026-11-14 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
