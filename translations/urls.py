import re

from django.core.urlresolvers import LocaleRegexURLResolver
from django.utils.translation import get_language

from .utils import get_default_language


class TranslationRegexURLResolver(LocaleRegexURLResolver):
    """
    A URL resolver that always matches the active language code as URL prefix.

    Rather than taking a regex argument, we just override the ``regex``
    function to always return the active language-code as regex.
    """

    @property
    def regex(self):
        if get_language() == get_default_language():
            return re.compile(r'')
        return super(TranslationRegexURLResolver, self).regex
