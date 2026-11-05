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

### 1. [Canadian Extradited to US Over Cryptomining Hacks on University Supercomputers](<https://www.securityweek.com/canadian-extradited-to-us-over-cryptomining-hacks-on-university-supercomputers/>)

**SecurityWeek** · News · Nov 04, 2026

Prosecutors allege Ryan James Roach and Mathiew James Stubbings compromised university systems in four U.S. states from 2016 to 2019, using stolen credentials, malware, and multi-country virtual servers to conceal their activity and mine Electroneum on hijacked university hardware.

[Read article →](<https://www.securityweek.com/canadian-extradited-to-us-over-cryptomining-hacks-on-university-supercomputers/>)

---

### 2. [Poisoned cPGuard update hits thousands of web hosting servers](<https://www.helpnetsecurity.com/2026/11/04/cpguard-update-supply-chain-compromised/>)

**Help Net Security** · News · Nov 04, 2026

A compromised cPGuard update channel delivered malicious versions 5.88.12–5.88.19 to about 2,950 servers, where agents ran the script as root. It exfiltrated sensitive files, including password hashes, SSH keys, database credentials, shell history, and cloud keys, and left a hidden root shell and scheduled task.

[Read article →](<https://www.helpnetsecurity.com/2026/11/04/cpguard-update-supply-chain-compromised/>)

---

### 3. [Synaptics Appears To Use Legal Threats To Block Open-Source DisplayLink Driver](<https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver>)

**Phoronix** · News · Nov 04, 2026

An experimental, clean-room Rust driver for modern DisplayLink hardware called Vino is no longer publicly available after Synaptics reportedly sent its developer a cease-and-desist notice alleging patent infringement.

[Read article →](<https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver>)

---

### 4. ["AMD Loves Omarchy" Linux With More Collaboration Coming](<https://www.phoronix.com/news/AMD-Loves-Omarchy>)

**Phoronix** · News · Nov 04, 2026

AMD VP of AI Software Anush Elangovan has praised Omarchy and met its lead, David Heinemeier Hansson, at the Fireworks Forge event, where he supplied him with an AMD-powered HP ZBook. Elangovan said “AMD ❤️ Omarchy.

[Read article →](<https://www.phoronix.com/news/AMD-Loves-Omarchy>)

---

### 5. [Chrome 157 Rolls Out With 213 Security Fixes, Seven Rated Critical](<https://www.securityweek.com/chrome-157-rolls-out-with-213-security-fixes-seven-rated-critical/>)

**SecurityWeek** · News · Nov 04, 2026

Chrome 157 fixes 213 vulnerabilities, including seven critical memory-safety flaws and 77 high-severity issues. The critical bugs include a Dawn buffer overflow ($10,000 bounty), an ANGLE memory-corruption flaw ($1,000), four use-after-free defects, and another buffer overflow.

[Read article →](<https://www.securityweek.com/chrome-157-rolls-out-with-213-security-fixes-seven-rated-critical/>)


---

Updated 2026-11-05 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
