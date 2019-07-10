# perf-map-agent-rpms
Spec files to build [perf-map-agent](https://github.com/jvm-profiling-tools/perf-map-agent) rpm

## Building

```
rpmbuild -ba --nodeps --define "_sourcedir $(pwd)" --define "_srcrpmdir $(pwd)" perf-map-agent.spec

```

## License
Public domain.

