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

### 1. [Windows 0-Day Dropped By Disgruntled Researcher Hands Hackers System Rights](<https://it.slashdot.org/story/26/11/14/020218/windows-0-day-dropped-by-disgruntled-researcher-hands-hackers-system-rights>)

**Slashdot** · News

SignDrop is a reported Windows Common Log File System vulnerability that can let an ordinary local user gain System rights by inducing a privileged process, such as Windows Defender, to open a crafted CLFS container.

[Read article →](<https://it.slashdot.org/story/26/11/14/020218/windows-0-day-dropped-by-disgruntled-researcher-hands-hackers-system-rights>)

---

### 2. [How to classify MCP tools by risk (read, edit, delete)](<https://nirmata.com/2026/11/16/classifying-mcp-tools-by-risk/>)

**Nirmata** · Article

Classify MCP tools by reviewed behavior: read tools change nothing, edit tools add or update state, and delete tools may destroy or overwrite it.

[Read article →](<https://nirmata.com/2026/11/16/classifying-mcp-tools-by-risk/>)

---

### 3. [Borland C++ 2.0 Compiler Source Reconstructed](<https://hackaday.com/2026/11/13/borland-c-2-0-compiler-source-reconstructed/>)

**Hackaday** · News · Nov 14, 2026

Borland C++ 2.0’s source has been reconstructed from the original toolchain binaries. The project claims the recreated source is byte-perfect in the practical sense that it produces binaries identical to those from the original compiler.

[Read article →](<https://hackaday.com/2026/11/13/borland-c-2-0-compiler-source-reconstructed/>)

---

### 4. [Desktop operating systems for ESP32-P4-based “PCs” – Meet Sylphide OS and Bare Metal, Do Stuff (BMDS)](<https://www.cnx-software.com/2026/11/14/desktop-operating-systems-for-esp32-p4-based-pcs-meet-sylphide-os-and-bare-metal-do-stuff-bmds/>)

**CNX Software – Embedded Systems News** · News · Nov 14, 2026

Sylphide OS and Bare Metal, Do Stuff (BMDS) bring desktop environments to microcontroller boards, with both projects targeting the Olimex ESP32-P4-PC. Sylphide uses FreeRTOS and offers a monochrome Macintosh-like interface, window manager, hardware drivers, and configuration framework.

[Read article →](<https://www.cnx-software.com/2026/11/14/desktop-operating-systems-for-esp32-p4-based-pcs-meet-sylphide-os-and-bare-metal-do-stuff-bmds/>)

---

### 5. [Attackers use Crypto Exchange Names to Disguise Unauthorized Sessions on 100+ ScreenConnect Servers](<https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect>)

**Cyber Newsroom** · News · Nov 14, 2026

Huntress found 2,223 unauthorized crypto-themed guest sessions on 118 ScreenConnect servers across 109 organizations, added between Nov. 3 and 13, 2026. The sessions were repeatedly kept online, but investigators observed no malicious guest activity.

[Read article →](<https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect>)


---

Updated 2026-11-15 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
