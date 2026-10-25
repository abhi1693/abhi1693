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

### 1. [Linux 7.4 Block Updates Range From Floppy Disk Driver Fixes To Apple M4 NVMe Support](<https://www.phoronix.com/news/Linux-7.4-Block>)

**Phoronix** · News · Oct 25, 2026

Linux 7.4’s merged block updates include fixes spanning legacy floppy hardware and newer Apple storage. The floppy driver received a stack out-of-bounds fix, correction of a regression affecting drive-structure flags, and fixes for data races identified by unspecified tools.

[Read article →](<https://www.phoronix.com/news/Linux-7.4-Block>)

---

### 2. [This AI Assistant Looks Like a Tiny Monitor but Actually Operates Your Computer](<https://www.yankodesign.com/2026/10/24/this-ai-assistant-looks-like-a-tiny-monitor-but-actually-operates-your-computer/>)

**Yanko Design** · Article · Oct 24, 2026

Bvio’s Violoop is a plug-in AI operator that uses screen understanding and keyboard and mouse controls to carry out repetitive tasks in existing apps, such as moving details from WhatsApp into a CRM, preparing spreadsheet entries, organizing files, and drafting email replies.

[Read article →](<https://www.yankodesign.com/2026/10/24/this-ai-assistant-looks-like-a-tiny-monitor-but-actually-operates-your-computer/>)

---

### 3. [2026 Retrocomputing Challenge: I Would Do Anything For Serial Data](<https://hackaday.com/2026/10/24/2026-retrocomputing-challenge-i-would-do-anything-for-serial-data/>)

**Hackaday** · News · Oct 24, 2026

Meatloaf uses an ESP32 connected to a Commodore computer’s IEC serial port to deliver files from local storage or active URLs. A dedicated service points to files regardless of where they are stored; the device retrieves them and sends them over the serial link.

[Read article →](<https://hackaday.com/2026/10/24/2026-retrocomputing-challenge-i-would-do-anything-for-serial-data/>)

---

### 4. [CVE-2026-114820 - Vulnerability in the Oracle Java SE, Oracle GraalV](<https://cvefeed.io/vuln/detail/CVE-2026-114820>)

**Latest High/Critical Vulnerabilitiy Feed** · Article · Oct 24, 2026

CVE-2026-114820 affects the JSSE component in listed Oracle Java SE versions (8u511-b32, 8u511-perf-b32, 11.0.33.0.2, 17.0.21.0.2, 21.0.13.0.2, 25.0.5.0.2, 27.0.1.0.2), Oracle GraalVM for JDK 17.0.21.0.2 and 21.0.13.0.2, and GraalVM Enterprise Edition 21.3.20.0.2.

[Read article →](<https://cvefeed.io/vuln/detail/CVE-2026-114820>)

---

### 5. [The AI graveyard: a running list of projects and startups that didn’t make it](<https://techcrunch.com/2026/10/24/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/>)

**TechCrunch | AI News &#38; Artificial Intelligence** · News · Oct 24, 2026

The excerpt shows that AI projects can lose their footing for different reasons: Relay and Huxe faced competition from larger platforms adding similar features; Yupp lacked product-market fit, while Figgs AI said the cost of keeping its service free was unsustainable.

[Read article →](<https://techcrunch.com/2026/10/24/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/>)


---

Updated 2026-10-25 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
