# Share session scratch through delegation

Use one temporary-files directory per top-level session, namespaced by harness. The main agent selects it and every delegating agent passes the same absolute path downstream, so nested agents can exchange files without scattering them across unrelated child-session directories.

Keep the persistent research cache of the `external-research` skill shared across sessions and harnesses, separate from session scratch. Authorize these directories narrowly and keep shared skills read-only through native controls where available; do not substitute prompt restrictions for filesystem enforcement.
