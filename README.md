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

### 1. [CVE-2026-120317 - http4k 4.9.10.0 before 6.60.0.0 Digest auth-int Missing Body Integrity](<https://cvefeed.io/vuln/detail/CVE-2026-120317>)

**Latest High/Critical Vulnerabilitiy Feed** · News · Nov 02, 2026

http4k versions 4.9.10.0 up to but not including 6.60.0.0 have a missing integrity check in DigestEncoder: the auth-int digest is computed without hashing the request body.

[Read article →](<https://cvefeed.io/vuln/detail/CVE-2026-120317>)

---

### 2. [Experts Expect 'Security Reckoning' As AI Tools Find And Exploit Software Bugs](<https://it.slashdot.org/story/26/11/02/033200/experts-expect-security-reckoning-as-ai-tools-find-and-exploit-software-bugs>)

**Slashdot** · News

CrowdStrike attributed attacks exposing financial data at nine or more South Korean banks to an alleged amateur who used AI chatbots.

[Read article →](<https://it.slashdot.org/story/26/11/02/033200/experts-expect-security-reckoning-as-ai-tools-find-and-exploit-software-bugs>)

---

### 3. [CVE-2026-120277 - WAVLINK WN536AX6-A WireGuard CLI Group ioos sub&#95;41a1d8 os command injection](<https://cvefeed.io/vuln/detail/CVE-2026-120277>)

**Latest High/Critical Vulnerabilitiy Feed** · News · Nov 02, 2026

CVE-2026-120277 is rated critical (10.0) and affects WAVLINK WN536AX6-A running V260507&#95;2.0.0. The issue is in sub&#95;41a1d8 in /bin/ioos, part of the WireGuard CLI Group Handler: manipulating the group&#95;name argument can cause OS command injection.

[Read article →](<https://cvefeed.io/vuln/detail/CVE-2026-120277>)

---

### 4. [WiCi One Wants to Put a Wireless GPU in Your Homelab](<https://noted.lol/wici-one-wireless-gpu-homelab/>)

**Noted** · Article · Nov 02, 2026

WiCi One is a standalone computer that shares its NVIDIA GPU with nearby devices over Wi-Fi 7, either through virtual GPU support in compatible applications or an OpenAI-compatible API.

[Read article →](<https://noted.lol/wici-one-wireless-gpu-homelab/>)

---

### 5. [Cheap FPGA Board Becomes Retro-Style Computer](<https://hackaday.com/2026/11/01/cheap-fpga-board-becomes-retro-style-computer/>)

**Hackaday** · News · Nov 02, 2026

The roughly $15 Tang Nano 9K, built around a Gowin GW1NR-9C FPGA with 8,640 LUTs, can run a 36 MHz RISC-V CPU with 8 MB RAM, HDMI, stereo audio, USB, and SD card support.

[Read article →](<https://hackaday.com/2026/11/01/cheap-fpga-board-becomes-retro-style-computer/>)


---

Updated 2026-11-02 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
