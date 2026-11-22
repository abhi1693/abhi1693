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

### 1. [Borealis Isolated Postgres: Serious Database Security for the Common Runtime](<https://www.heroku.com/blog/borealis-isolated-postgres/>)

**Heroku** · Article · Nov 20, 2026

Borealis Isolated Postgres provides network-isolated PostgreSQL for apps on Heroku’s Common Runtime. Each database cluster sits in its own VPC and rejects incoming traffic by default, while three access paths support different needs: a buildpack creates secure app-to-database tunnels and can use a read-only URL…

[Read article →](<https://www.heroku.com/blog/borealis-isolated-postgres/>)

---

### 2. [CVE-2026-77329 - Tapo: DNS rebinding reaches unauthenticated Tapo MCP smart-home controls](<https://cvefeed.io/vuln/detail/CVE-2026-77329>)

**Latest High/Critical Vulnerabilitiy Feed** · News · Nov 20, 2026

From versions 0.3.1 to before 0.5.0, Tapo’s Streamable HTTP MCP server could accept DNS-rebound browser requests without Host or Origin validation when TAPO&#95;MCP&#95;API&#95;KEY was unset.

[Read article →](<https://cvefeed.io/vuln/detail/CVE-2026-77329>)

---

### 3. [CVE-2026-133874 - Iceburg CRM through 5.0.0 Authorization Bypass via Record Save](<https://cvefeed.io/vuln/detail/CVE-2026-133874>)

**Latest High/Critical Vulnerabilitiy Feed** · Article · Nov 20, 2026

Iceburg CRM through version 5.0.0 has an authorization flaw in Module::saveRecord() that can let authenticated users write to modules they are not authorized to access.

[Read article →](<https://cvefeed.io/vuln/detail/CVE-2026-133874>)

---

### 4. [Google Is Putting AI Chats Right On the Homepage](<https://tech.slashdot.org/story/26/11/20/0138234/google-is-putting-ai-chats-right-on-the-homepage>)

**Slashdot** · News

Google is rolling out a redesigned desktop homepage with a collapsible sidebar that lets users return to and continue previous AI Mode searches.

[Read article →](<https://tech.slashdot.org/story/26/11/20/0138234/google-is-putting-ai-chats-right-on-the-homepage>)

---

### 5. [Java4Shell (CVE-2026-114938): What It Means for TeamCity](<https://blog.jetbrains.com/teamcity/2026/11/java4shell-cve-2026-114938-what-it-means-for-teamcity/>)

**JetBrains** · News · Nov 20, 2026

CVE-2026-114938 is a memory-corruption flaw in an optimized Java Base64 decoder, not in TeamCity itself.

[Read article →](<https://blog.jetbrains.com/teamcity/2026/11/java4shell-cve-2026-114938-what-it-means-for-teamcity/>)


---

Updated 2026-11-22 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
