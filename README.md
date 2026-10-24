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

### 1. [PowerToys adds smarter mouse controls and more Windows customization](<https://www.techspot.com/downloads/7185-microsoft-powertoys.html>)

**TechSpot** · Release · Oct 24, 2026

PowerToys 0.102 adds controls for common input and workflow tasks. Mouse Button Lock lets a long press keep a mouse button active for dragging or selecting until another click; CursorHide hides the pointer during typing or inactivity and restores it on mouse movement.

[Read article →](<https://www.techspot.com/downloads/7185-microsoft-powertoys.html>)

---

### 2. [The last 24 hours in PHP land, as observed by a monitoring service](<https://freek.dev/3207-the-last-24-hours-in-php-land-as-observed-by-a-monitoring-service>)

**Freek** · News · Oct 24, 2026

Oh Dear reports that site outages peaked at 18.8% during the recent critical PHP vulnerabilities, while down alerts rose to 25 times their normal level.

[Read article →](<https://freek.dev/3207-the-last-24-hours-in-php-land-as-observed-by-a-monitoring-service>)

---

### 3. [CVE-2026-116011 - Crow before 1.3.4 Denial of Service via Deeply Nested JSON in crow::json::load()](<https://cvefeed.io/vuln/detail/CVE-2026-116011>)

**Latest High/Critical Vulnerabilitiy Feed** · News · Oct 24, 2026

Crow versions before 1.3.4 have an uncontrolled recursion flaw in &#96;crow::json::load()&#96;. A remote unauthenticated attacker can send a request body containing thousands of nested JSON objects, exhaust the worker thread stack, crash the server process, and drop all connections.

[Read article →](<https://cvefeed.io/vuln/detail/CVE-2026-116011>)

---

### 4. [Meet Anthropic’s sandbox-runtime: OS-Level Sandboxing for AI Agents, No Containers](<https://www.marktechpost.com/2026/10/24/anthropic-sandbox-runtime-ai-agent-sandbox/>)

**MarkTechPost** · Article · Oct 24, 2026

Anthropic’s open-source sandbox-runtime (srt) wraps processes in OS-level file and network restrictions, including their subprocesses, without containers. It can run as a CLI or TypeScript library for agents, MCP servers, and other commands.

[Read article →](<https://www.marktechpost.com/2026/10/24/anthropic-sandbox-runtime-ai-agent-sandbox/>)

---

### 5. [systemd Merges Support For Rust Programs](<https://www.phoronix.com/news/systemd-Merges-Rust-Programs>)

**Phoronix** · News · Oct 24, 2026

systemd has merged optional Rust support for leaf programs, while core systemd code such as the systemd library still lacks Rust support pending resolution of blockers. Rust components are built with Meson without Cargo, and C linkage is required.

[Read article →](<https://www.phoronix.com/news/systemd-Merges-Rust-Programs>)


---

Updated 2026-10-24 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
