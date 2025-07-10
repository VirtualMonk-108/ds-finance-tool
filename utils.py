# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import textwrap

import streamlit as st


def show_code(demo):
    """Showing the code of the demo."""
    # show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))
# Version update 1
# Version update 5
# Version update 9
# Version update 13
# Update 2025-01-01-5
# Update 2025-01-03-2
# Update 2025-01-07-1
# Update 2025-01-09-2
# Update 2025-01-10-1
# Update 2025-01-14-3
# Update 2025-01-15-1
# Update 2025-01-16-1
# Update 2025-01-16-5
# Update 2025-01-17-1
# Update 2025-01-17-3
# Update 2025-01-21-1
# Update 2025-01-24-1
# Update 2025-01-25-1
# Update 2025-01-29-4
# Update 2025-01-29-5
# Update 2025-01-30-1
# Update 2025-01-31-2
# Update 2025-02-01-2
# Update 2025-02-06-2
# Update 2025-02-07-2
# Update 2025-02-11-2
# Update 2025-02-12-1
# Update 2025-02-14-2
# Update 2025-02-17-6
# Update 2025-02-21-1
# Update 2025-02-21-2
# Update 2025-02-21-3
# Update 2025-02-24-1
# Update 2025-02-24-3
# Update 2025-02-25-2
# Update 2025-02-27-2
# Update 2025-03-02-1
# Update 2025-03-02-2
# Update 2025-03-03-4
# Update 2025-03-04-2
# Update 2025-03-06-1
# Update 2025-03-07-1
# Update 2025-03-07-2
# Update 2025-03-13-1
# Update 2025-03-13-2
# Update 2025-03-14-2
# Update 2025-03-17-1
# Update 2025-03-21-5
# Update 2025-03-24-1
# Update 2025-03-25-1
# Update 2025-03-25-4
# Update 2025-03-26-1
# Update 2025-03-27-4
# Update 2025-03-31-1
# Update 2025-04-02-1
# Update 2025-04-04-1
# Update 2025-04-08-1
# Update 2025-04-10-1
# Update 2025-04-12-2
# Update 2025-04-16-2
# Update 2025-04-25-1
# Update 2025-04-25-3
# Update 2025-04-26-1
# Update 2025-04-28-1
# Update 2025-05-01-4
# Update 2025-05-03-1
# Update 2025-05-07-1
# Update 2025-05-11-1
# Update 2025-05-13-2
# Update 2025-05-13-3
# Update 2025-05-14-2
# Update 2025-05-16-1
# Update 2025-05-17-1
# Update 2025-05-19-2
# Update 2025-05-19-3
# Update 2025-05-21-1
# Update 2025-05-22-2
# Update 2025-05-23-1
# Update 2025-05-25-1
# Update 2025-05-26-1
# Update 2025-05-30-2
# Update 2025-05-30-3
# Update 2025-06-05-2
# Update 2025-06-09-1
# Update 2025-06-09-2
# Update 2025-06-10-1
# Update 2025-06-13-3
# Update 2025-06-16-3
# Update 2025-06-17-1
# Update 2025-06-19-2
# Update 2025-06-24-2
# Update 2025-06-30-1
# Update 2025-07-07-6
# Update 2025-07-09-1
# Update 2025-07-09-3
# Update 2025-07-10-1
# Update 2025-07-10-2
