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
