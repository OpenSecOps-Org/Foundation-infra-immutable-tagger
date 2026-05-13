# Change Log

## v1.2.3
    * Security: bump `urllib3` floor to `>=2.7.0` in `boto3.in` (distributed from canonical `Installer/templates/boto3.in`) to remediate CVE-2026-44431 and CVE-2026-44432 (both affect urllib3 ≤ 2.6.3, fixed in 2.7.0). The pinned `boto3==1.42.94` previously resolved urllib3 transitively to 2.6.3; the new floor forces resolution to 2.7.0. Locks recompiled with `--upgrade`; other transitive deps refreshed to their latest in-range versions as a side effect (no code or behaviour change).

## v1.2.2
    * Enable auto-close workflow for external pull requests, enforcing the cathedral governance policy uniformly across all OpenSecOps repositories. Pull requests from non-team authors are closed automatically with a redirect comment pointing to the bug-report template, the GitHub Security Advisory flow, and the fork-under-MPL-2.0 path.
    * `SECURITY.md` §14 now carries a Trust-page cross-link ([opensecops.org/trust.html](https://www.opensecops.org/trust.html)) alongside the existing canonical supply-chain document link, positioning the Trust page as the lighter customer-facing synthesis.

## v1.2.1

- `SECURITY.md` and `README` updated re: OpenSSF Scorecard publication status. See [supply-chain documentation](https://github.com/OpenSecOps-Org/Documentation/blob/main/docs/security/supply-chain.md) §5.5.

## v1.2.0
    * Converted to OpenSecOps supply-chain framework: hash-pinned dependencies, signed releases, daily CVE scan, Scorecard. See `SECURITY.md`.
    * `boto3` now hash-pinned to `1.42.94` per project-wide pin policy (previously implicit from Lambda runtime).

## v1.1.7
    * Updated GitHub remote references in publish.zsh script to use only OpenSecOps-Org, removed Delegat-AB

## v1.1.6
    * Updated GitHub organization name from CloudSecOps-Org to OpenSecOps-Org.
    * Updated references to CloudSecOps-Installer to Installer.

## v1.1.5
    * File paths corrected for the new name of the installer.

## v1.1.4
    * Updated LICENSE file to MPL 2.0.

## v1.1.3
    * Updated publish.zsh to support dual-remote publishing to CloudSecOps-Org repositories.

## v1.1.2
    * `.python-version` file added for pyenv.

## v1.1.1
    * Updated the README.

## v1.1.0
    * Added task to tag CloudWatch alarms, due to AWS' latest changes.
    * Switched to Python 3.12.

## v1.0.4
    * Refreshed scripts.

## v1.0.3
    * Open-source credits and URLs
    * Fixed installer initial stackset creation.

## v1.0.2
    * Merge fix.

## v1.0.1
    * `--dry-run` and `--verbose` added to `deploy`.

## v1.0.0
    * Initial release.
