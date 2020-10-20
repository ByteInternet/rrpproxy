from unittest.case import TestCase

from rrpproxy.utils.status_codes import COMMAND_COMPLETED_SUCCESSFULLY, DOMAIN_NAME_AVAILABLE, \
    DOMAIN_NAME_NOT_AVAILABLE, NAME_SERVER_AVAILABLE, NAME_SERVER_NOT_AVAILABLE, CONTACT_AVAILABLE, \
    CONTACT_NOT_AVAILABLE, OBJECT_AVAILABLE, OBJECT_NOT_AVAILABLE, REQUEST_AVAILABLE, REQUEST_NOT_AVAILABLE, \
    COMMAND_COMPLETED_SUCCESSFULLY_CLOSING_CONNECTION, SERVER_ERROR_CLOSING_CONNECTION, \
    SERVER_ERROR_CLIENT_SHOULD_TRY_AGAIN, ABUSE_DETECTED, SOCKET_ERROR, INVALID_COMMAND_NAME, INVALID_COMMAND_OPTION, \
    INVALID_ENTITY_VALUE, INVALID_ATTRIBUTE_NAME, MISSING_REQUIRED_ATTRIBUTE, INVALID_ATTRIBUTE_VALUE_SYNTAX, \
    INVALID_OPTION_VALUE, INVALID_COMMAND_FORMAT, MISSING_REQUIRED_ENTITY, MISSING_COMMAND_OPTION, \
    SERVER_CLOSING_CONNECTION_TRY_AGAIN, TOO_MANY_SESSIONS_OPEN_CLOSING_CONNECTION, AUTHENTICATION_FAILED, \
    AUTHORIZATION_FAILED, DOMAIN_NAMES_LINKED_WITH_NAME_SERVER, DOMAIN_NAME_HAS_ACTIVE_NAME_SERVERS, \
    DOMAIN_NAME_NOT_FLAGGED_FOR_TRANSFER, RESTRICTED_IP_ADDRESS, DOMAIN_ALREADY_FLAGGED_FOR_TRANSFER, \
    ATTRIBUTE_VALUE_NOT_UNIQUE, INVALID_ATTRIBUTE_VALUE, INVALID_OLD_ATTRIBUTE_VALUE, \
    FINAL_OR_IMPLICIT_ATTRIBUTE_CANNOT_BE_UPDATED, ENTITY_ON_HOLD, ENTITY_REFERENCE_NOT_FOUND, CREDIT_LIMIT_EXCEEDED, \
    INVALID_COMMAND_SEQUENCE, DOMAIN_NOT_UP_FOR_RENEWAL, COMMAND_FAILED, PARENT_DOMAIN_NOT_REGISTERED, \
    PARENT_DOMAIN_STATUS_DOES_NOT_ALLOW_OPERATION, DOMAIN_STATUS_DOES_NOT_ALLOW_OPERATION, \
    OPERATION_NOT_ALLOWED_DOMAIN_PENDING_TRANSFER, DOMAIN_ALREADY_REGISTERED, DOMAIN_ALREADY_RENEWED, \
    MAXIMUM_REGISTRATION_PERIOD_EXCEEDED, OBJECT_STATUS_PROHIBITS_OPERATION, RESOURCE_DISABLED, RESOURCE_STILL_IN_USE, \
    EMAIL_ADDRESS_ALREADY_USES_FORWARDING, EMAIL_ADDRESS_ALREADY_USES_MAILSPACE, \
    EMAIL_DOMAIN_ALREADY_LINKED_TO_DIFFERENT_MAILSPACE


class TestStatusCodes(TestCase):
    def test_command_completed_succesfully_is_200(self):
        self.assertEqual(COMMAND_COMPLETED_SUCCESSFULLY, 200)

    def test_domain_name_available_is_210(self):
        self.assertEqual(DOMAIN_NAME_AVAILABLE, 210)

    def test_domain_name_not_available_is_211(self):
        self.assertEqual(DOMAIN_NAME_NOT_AVAILABLE, 211)

    def test_name_server_available_is_212(self):
        self.assertEqual(NAME_SERVER_AVAILABLE, 212)

    def test_name_server_not_available_is_213(self):
        self.assertEqual(NAME_SERVER_NOT_AVAILABLE, 213)

    def test_contact_available_is_214(self):
        self.assertEqual(CONTACT_AVAILABLE, 214)

    def test_contact_not_available_is_215(self):
        self.assertEqual(CONTACT_NOT_AVAILABLE, 215)

    def test_object_available_is_216(self):
        self.assertEqual(OBJECT_AVAILABLE, 216)

    def test_object_not_available_is_217(self):
        self.assertEqual(OBJECT_NOT_AVAILABLE, 217)

    def test_request_available_is_218(self):
        self.assertEqual(REQUEST_AVAILABLE, 218)

    def test_request_not_available_is_219(self):
        self.assertEqual(REQUEST_NOT_AVAILABLE, 219)

    def test_command_completed_successfully_closing_connection_is_220(self):
        self.assertEqual(COMMAND_COMPLETED_SUCCESSFULLY_CLOSING_CONNECTION, 220)

    def test_server_error_closing_connection_is_420(self):
        self.assertEqual(SERVER_ERROR_CLOSING_CONNECTION, 420)

    def test_server_error_client_should_try_again_is_421(self):
        self.assertEqual(SERVER_ERROR_CLIENT_SHOULD_TRY_AGAIN, 421)

    def test_abuse_detected_is_422(self):
        self.assertEqual(ABUSE_DETECTED, 422)

    def test_socket_error_is_423(self):
        self.assertEqual(SOCKET_ERROR, 423)

    def test_invalid_command_name_is_500(self):
        self.assertEqual(INVALID_COMMAND_NAME, 500)

    def test_invalid_command_option_is_501(self):
        self.assertEqual(INVALID_COMMAND_OPTION, 501)

    def test_invalid_entity_value_is_502(self):
        self.assertEqual(INVALID_ENTITY_VALUE, 502)

    def test_invalid_attribute_name_is_503(self):
        self.assertEqual(INVALID_ATTRIBUTE_NAME, 503)

    def test_missing_required_attribute_is_504(self):
        self.assertEqual(MISSING_REQUIRED_ATTRIBUTE, 504)

    def test_invalid_attribute_value_syntax_is_505(self):
        self.assertEqual(INVALID_ATTRIBUTE_VALUE_SYNTAX, 505)

    def test_invalid_option_value_is_506(self):
        self.assertEqual(INVALID_OPTION_VALUE, 506)

    def test_invalid_command_format_is_507(self):
        self.assertEqual(INVALID_COMMAND_FORMAT, 507)

    def test_missing_required_entity_is_508(self):
        self.assertEqual(MISSING_REQUIRED_ENTITY, 508)

    def test_missing_command_option_is_509(self):
        self.assertEqual(MISSING_COMMAND_OPTION, 509)

    def test_server_closing_connection_try_again_is_520(self):
        self.assertEqual(SERVER_CLOSING_CONNECTION_TRY_AGAIN, 520)

    def test_too_many_sessions_open_closing_connection_is_521(self):
        self.assertEqual(TOO_MANY_SESSIONS_OPEN_CLOSING_CONNECTION, 521)

    def test_authentication_failed_is_530(self):
        self.assertEqual(AUTHENTICATION_FAILED, 530)

    def test_authorization_failed_is_531(self):
        self.assertEqual(AUTHORIZATION_FAILED, 531)

    def test_domain_names_linked_with_name_server_is_532(self):
        self.assertEqual(DOMAIN_NAMES_LINKED_WITH_NAME_SERVER, 532)

    def test_domain_name_has_active_name_servers_is_533(self):
        self.assertEqual(DOMAIN_NAME_HAS_ACTIVE_NAME_SERVERS, 533)

    def test_domain_name_not_flagged_for_transfer_is_534(self):
        self.assertEqual(DOMAIN_NAME_NOT_FLAGGED_FOR_TRANSFER, 534)

    def test_restricted_ip_address_is_535(self):
        self.assertEqual(RESTRICTED_IP_ADDRESS, 535)

    def test_domain_already_flagged_for_transfer_is_536(self):
        self.assertEqual(DOMAIN_ALREADY_FLAGGED_FOR_TRANSFER, 536)

    def test_attribute_value_not_unique_is_540(self):
        self.assertEqual(ATTRIBUTE_VALUE_NOT_UNIQUE, 540)

    def test_invalid_attribute_value_is_541(self):
        self.assertEqual(INVALID_ATTRIBUTE_VALUE, 541)

    def test_invalid_old_attribute_value_is_542(self):
        self.assertEqual(INVALID_OLD_ATTRIBUTE_VALUE, 542)

    def test_final_or_implicit_attribute_cannot_be_updated_is_543(self):
        self.assertEqual(FINAL_OR_IMPLICIT_ATTRIBUTE_CANNOT_BE_UPDATED, 543)

    def test_entity_on_hold_is_544(self):
        self.assertEqual(ENTITY_ON_HOLD, 544)

    def test_entity_reference_not_found_is_545(self):
        self.assertEqual(ENTITY_REFERENCE_NOT_FOUND, 545)

    def test_credit_limit_exceeded_is_546(self):
        self.assertEqual(CREDIT_LIMIT_EXCEEDED, 546)

    def test_invalid_command_sequence_is_547(self):
        self.assertEqual(INVALID_COMMAND_SEQUENCE, 547)

    def test_domain_not_up_for_renewal_is_548(self):
        self.assertEqual(DOMAIN_NOT_UP_FOR_RENEWAL, 548)

    def test_command_failed_is_549(self):
        self.assertEqual(COMMAND_FAILED, 549)

    def test_parent_domain_not_registered_is_550(self):
        self.assertEqual(PARENT_DOMAIN_NOT_REGISTERED, 550)

    def test_parent_domain_status_does_not_allow_operation_is_551(self):
        self.assertEqual(PARENT_DOMAIN_STATUS_DOES_NOT_ALLOW_OPERATION, 551)

    def test_domain_status_does_not_allow_operation_is_552(self):
        self.assertEqual(DOMAIN_STATUS_DOES_NOT_ALLOW_OPERATION, 552)

    def test_operation_not_allowed_domain_pending_transfer_is_553(self):
        self.assertEqual(OPERATION_NOT_ALLOWED_DOMAIN_PENDING_TRANSFER, 553)

    def test_domain_already_registered_is_554(self):
        self.assertEqual(DOMAIN_ALREADY_REGISTERED, 554)

    def test_domain_already_renewed_is_555(self):
        self.assertEqual(DOMAIN_ALREADY_RENEWED, 555)

    def test_maximum_registration_period_exceeded_is_556(self):
        self.assertEqual(MAXIMUM_REGISTRATION_PERIOD_EXCEEDED, 556)

    def test_object_status_prohibits_operation_is_557(self):
        self.assertEqual(OBJECT_STATUS_PROHIBITS_OPERATION, 557)

    def test_resource_disabled_is_560(self):
        self.assertEqual(RESOURCE_DISABLED, 560)

    def test_resource_still_in_use_is_561(self):
        self.assertEqual(RESOURCE_STILL_IN_USE, 561)

    def test_email_address_already_uses_forwarding_is_562(self):
        self.assertEqual(EMAIL_ADDRESS_ALREADY_USES_FORWARDING, 562)

    def test_email_address_already_uses_mailspace_is_563(self):
        self.assertEqual(EMAIL_ADDRESS_ALREADY_USES_MAILSPACE, 563)

    def test_email_domain_already_linked_to_different_mailspace_is_564(self):
        self.assertEqual(EMAIL_DOMAIN_ALREADY_LINKED_TO_DIFFERENT_MAILSPACE, 564)
