# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from ibm_cloud_cis_services.firewall_access_rules_v1 import FirewallAccessRulesV1

crn = 'testString'

service = FirewallAccessRulesV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ListAllInstanceLevelAccessRules
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_account_access_rules
#-----------------------------------------------------------------------------
class TestListAllAccountAccessRules():

    #--------------------------------------------------------
    # list_all_account_access_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_account_access_rules_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        notes = 'testString'
        mode = 'block'
        configuration_target = 'ip'
        configuration_value = 'testString'
        page = 38
        per_page = 38
        order = 'target'
        direction = 'asc'
        match = 'any'

        # Invoke method
        response = service.list_all_account_access_rules(
            notes=notes,
            mode=mode,
            configuration_target=configuration_target,
            configuration_value=configuration_value,
            page=page,
            per_page=per_page,
            order=order,
            direction=direction,
            match=match
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'notes={}'.format(notes) in query_string
        assert 'mode={}'.format(mode) in query_string
        assert 'configuration.target={}'.format(configuration_target) in query_string
        assert 'configuration.value={}'.format(configuration_value) in query_string
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'match={}'.format(match) in query_string


    #--------------------------------------------------------
    # test_list_all_account_access_rules_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_account_access_rules_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_account_access_rules()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ListAllInstanceLevelAccessRules
##############################################################################

##############################################################################
# Start of Service: GetAnInstanceLevelAccessRule
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_account_access_rule
#-----------------------------------------------------------------------------
class TestGetAccountAccessRule():

    #--------------------------------------------------------
    # get_account_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_access_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.get_account_access_rule(
            accessrule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_account_access_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_access_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.get_account_access_rule(
            accessrule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetAnInstanceLevelAccessRule
##############################################################################

##############################################################################
# Start of Service: CreateAnInstanceLevelAccessRule
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_account_access_rule
#-----------------------------------------------------------------------------
class TestCreateAccountAccessRule():

    #--------------------------------------------------------
    # create_account_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_access_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AccessruleInputConfiguration model
        accessrule_input_configuration_model =  {
            'target': 'ip',
            'value': 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'
        }

        # Set up parameter values
        mode = 'block'
        notes = 'This rule is added because of event X that occurred on date xyz'
        configuration = accessrule_input_configuration_model

        # Invoke method
        response = service.create_account_access_rule(
            mode=mode,
            notes=notes,
            configuration=configuration,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == mode
        assert req_body['notes'] == notes
        assert req_body['configuration'] == configuration


    #--------------------------------------------------------
    # test_create_account_access_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_access_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_account_access_rule()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: CreateAnInstanceLevelAccessRule
##############################################################################

##############################################################################
# Start of Service: UpdateAnInstanceLevelAccessRule
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_account_access_rule
#-----------------------------------------------------------------------------
class TestUpdateAccountAccessRule():

    #--------------------------------------------------------
    # update_account_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_access_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'
        mode = 'block'
        notes = 'This rule is added because of event X that occurred on date xyz'

        # Invoke method
        response = service.update_account_access_rule(
            accessrule_identifier,
            mode=mode,
            notes=notes,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == mode
        assert req_body['notes'] == notes


    #--------------------------------------------------------
    # test_update_account_access_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_access_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.update_account_access_rule(
            accessrule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateAnInstanceLevelAccessRule
##############################################################################

##############################################################################
# Start of Service: DeleteAnInstanceLevelAccessRule
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for delete_account_access_rule
#-----------------------------------------------------------------------------
class TestDeleteAccountAccessRule():

    #--------------------------------------------------------
    # delete_account_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_account_access_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.delete_account_access_rule(
            accessrule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_account_access_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_account_access_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/firewall/access_rules/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.delete_account_access_rule(
            accessrule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: DeleteAnInstanceLevelAccessRule
##############################################################################

