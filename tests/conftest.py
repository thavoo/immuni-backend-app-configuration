#    Copyright (C) 2020 Presidenza del Consiglio dei Ministri.
#    Please refer to the AUTHORS file for more information.
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.

from immuni_app_configuration.core import config
from immuni_common.helpers.tests import check_environment, check_mongo_url

# noinspection PyUnresolvedReferences
from tests.fixtures.core import *  # noqa isort:skip

# noinspection PyUnresolvedReferences
from tests.fixtures.setting import *  # noqa isort:skip

# noinspection PyUnresolvedReferences
from immuni_common.helpers.tests import monitoring_setup  # noqa isort:skip

check_environment()
check_mongo_url(config.APP_CONFIGURATION_MONGO_URL, "APP_CONFIGURATION_MONGO_URL")
