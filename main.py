

import config

if config.PRODUCTION:
    import gopigo_mockup
else:
    import gopigo_mockup as gopigo


