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

### 1. [November 2026 Patch Tuesday forecast: Old software continues to bite](<https://www.helpnetsecurity.com/2026/11/06/november-2026-patch-tuesday-forecast/>)

**Help Net Security** · News · Nov 06, 2026

The article’s practical takeaway is to patch actively exploited flaws promptly and keep removing obsolete software: even final-patched or abandoned apps can remain network-connected and expose systems.

[Read article →](<https://www.helpnetsecurity.com/2026/11/06/november-2026-patch-tuesday-forecast/>)

---

### 2. [Security certification is a snapshot, and buyers read too much into it](<https://www.helpnetsecurity.com/2026/11/06/mariia-bakhtina-masaryk-university-security-certification/>)

**Help Net Security** · Opinion · Nov 06, 2026

Common Criteria and FIPS 140 certificates document evaluation within a defined scope; they do not promise that a whole product is secure or free of vulnerabilities.

[Read article →](<https://www.helpnetsecurity.com/2026/11/06/mariia-bakhtina-masaryk-university-security-certification/>)

---

### 3. [87% say their AI controls need to work better](<https://www.helpnetsecurity.com/2026/11/06/autonomous-ai-oversight-governance/>)

**Help Net Security** · News · Nov 06, 2026

Among surveyed business decision-makers at companies with more than $500 million in annual revenue, over half say their teams’ AI can act within defined rules without routine review or complete processes without human approval; reported autonomy ranges from 54% for standalone generative tools to 59%…

[Read article →](<https://www.helpnetsecurity.com/2026/11/06/autonomous-ai-oversight-governance/>)

---

### 4. [99% of repository access tokens never expire](<https://www.helpnetsecurity.com/2026/11/06/blueflag-ai-agents-access-risks-report/>)

**Help Net Security** · News · Nov 06, 2026

BlueFlag Security’s 2026 report finds that repository credentials and developer access often outlast their purpose: 99% of measured repository access tokens had no expiration, 84% allowed code changes, and 47% had gone unused for over 90 days without revocation.

[Read article →](<https://www.helpnetsecurity.com/2026/11/06/blueflag-ai-agents-access-risks-report/>)

---

### 5. [Rental phishing sites use live chat to win over hesitant travelers](<https://www.helpnetsecurity.com/2026/11/06/holiday-rental-platform-phishing-travelers/>)

**Help Net Security** · News · Nov 06, 2026

Fake rental-booking sites copied familiar platform branding, property listings and reservation details, then used urgent claims about unconfirmed bookings, failed payments or cancellations to push travelers toward verification and payment.

[Read article →](<https://www.helpnetsecurity.com/2026/11/06/holiday-rental-platform-phishing-travelers/>)


---

Updated 2026-11-07 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
