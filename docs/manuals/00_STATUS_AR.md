# vaixlns-csd-kernel — كتيب التشغيل

الموجود حاليًا هو `VAIXLNS_ROOT.lns` مع parser/compiler مرجعيين قابلين للتشغيل، وتحويل المصدر إلى semantic IR حتمي.

الحالة التشغيلية الحالية:
IMPLEMENTED + TESTED (reference DSL subset).

أدلة التنفيذ:
- parser: `lns_kernel/parser.py`
- compiler: `lns_kernel/compiler.py`
- tests: `tests/test_lns_kernel.py`
- CI: Run `37391770207` — SUCCESS.

حدود الحالة:
- هذه الأدلة تثبت parser/compiler للجزء المغطّى بالاختبارات.
- لا تثبت بعد اكتمال اللغة كلها، ولا runtime كامل، ولا production certification.
