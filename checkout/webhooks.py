from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)


    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'account.application.authorized': handler.account.application.authorized,
        'account.application.deauthorized': handler.account.application.deauthorized,
        'account.external_account.created': handler.account.external_account.created,
        'account.external_account.deleted': handler.account.external_account.deleted,
        'account.external_account.updated': handler.account.external_account.updated,
        'account.updated': handler.account.updated,
        'application_fee.created': handler.application_fee.created,
        'application_fee.refund.updated': handler.application_fee.refund.updated,
        'application_fee.refunded': handler.application_fee.refunded,
        'balance.available': handler.balance.availabl,
        'billing_portal.configuration.created': handler.billing_portal.configuration.created,
        'billing_portal.configuration.updated': handler.billing_portal.configuration.updated,
        'capability.updated':handler.capability.updated,
        'charge.captured': handler.charge.captured,
        'charge.dispute.closed': handler.charge.dispute.closed,
        'charge.dispute.created': handler.charge.dispute.created,
        'charge.dispute.funds_reinstated': handler.charge.dispute.funds_reinstated,
        'charge.dispute.funds_withdrawn': handler.charge.dispute.funds_withdrawn,
        'charge.dispute.updated': handler.charge.dispute.updated,
        'charge.expired': handler.charge.expired,
        'charge.failed': handler.charge.failed,
        'charge.pending': handler.charge.pending,
        'charge.refund.updated': handler.charge.refund.updated,
        'charge.refunded': handler.charge.refunded,
        'charge.succeeded': handler.charge.succeeded,
        'charge.updated': handler.charge.updated,
        'checkout.session.async_payment_failed': handler.checkout.session.async_payment_failed,
        'checkout.session.async_payment_succeeded': handler.checkout.session.async_payment_succeeded,
        'checkout.session.completed': handler.checkout.session.completed,
        'checkout.session.expired': handler.checkout.session.expired,
        'coupon.created': handler.coupon.created,
        'coupon.deleted': handler.coupon.deleted,
        'coupon.updated': handler.coupon.updated,
        'credit_note.created': handler.credit_note.created,
        'credit_note.updated': handler.credit_note.updated,
        'credit_note.voided': handler.credit_note.voided,
        'customer.created': handler.customer.created,
        'customer.deleted': handler.customer.deleted,
        'customer.discount.created': handler.customer.discount.created,
        'customer.discount.deleted': handler.customer.discount.deleted,
        'customer.discount.updated': handler.customer.discount.updated,
        'customer.source.created': handler.customer.source.created,
        'customer.source.deleted': handler.customer.source.deleted,
        'customer.source.expiring': handler.customer.source.expiring,
        'customer.source.updated': handler.customer.source.updated,
        'customer.subscription.created': handler.customer.subscription.created,
        'customer.subscription.deleted': handler.customer.subscription.deleted,
        'customer.subscription.pending_update_applied': handler.customer.subscription.pending_update_applied,
        'customer.subscription.pending_update_expired': handler.customer.subscription.pending_update_expired,
        'customer.subscription.trial_will_end': handler.customer.subscription.trial_will_end,
        'customer.subscription.updated': handler.customer.subscription.updated,
        'customer.tax_id.created': handler.customer.tax_id.created,
        'customer.tax_id.deleted': handler.customer.tax_id.deleted,
        'customer.tax_id.updated': handler.customer.tax_id.updated,
        'customer.updated': handler.customer.updated,
        'file.created': handler.file.created,
        'identity.verification_session.canceled': handler.identity.verification_session.canceled,
        'identity.verification_session.created': handler.identity.verification_session.created,
        'identity.verification_session.processing': handler.identity.verification_session.processing,
        'identity.verification_session.redacted': handler.identity.verification_session.redacted,
        'identity.verification_session.requires_input': handler.identity.verification_session.requires_input,
        'identity.verification_session.verified': handler.identity.verification_session.verified,
        'invoice.created': handler.invoice.created,
        'invoice.deleted': handler.invoice.deleted,
        'invoice.finalization_failed': handler.invoice.finalization_failed,
        'invoice.finalized': handler.invoice.finalized,
        'invoice.marked_uncollectible': handler.invoice.marked_uncollectible,
        'invoice.paid': handler.invoice.paid,
        'invoice.payment_action_required': handler.invoice.payment_action_required,
        'invoice.payment_failed': handler.invoice.payment_failed,
        'invoice.payment_succeeded': handler.invoice.payment_succeeded,
        'invoice.sent': handler.invoice.sent,
        'invoice.upcoming': handler.invoice.upcoming,
        'invoice.updated': handler.invoice.updated,
        'invoice.voided': handler.invoice.voided,
        'invoiceitem.created': handler.invoiceitem.created,
        'invoiceitem.deleted': handler.invoiceitem.deleted,
        'invoiceitem.updated': handler.invoiceitem.updated,
        'issuing_authorization.created': handler.issuing_authorization.created,
        'issuing_authorization.request': handler.issuing_authorization.request,
        'issuing_authorization.updated': handler.issuing_authorization.updated,
        'issuing_card.created': handler.issuing_card.created,
        'issuing_card.updated': handler.issuing_card.updated,
        'issuing_cardholder.created': handler.issuing_cardholder.created,
        'issuing_cardholder.updated': handler.issuing_cardholder.updated,
        'issuing_dispute.closed': handler.issuing_dispute.closed,
        'issuing_dispute.created': handler.issuing_dispute.created,
        'issuing_dispute.funds_reinstated': handler.issuing_dispute.funds_reinstate,
        'issuing_dispute.submitted': handler.issuing_dispute.submitted,
        'issuing_dispute.updated': handler.issuing_dispute.updated,
        'issuing_transaction.created': handler.issuing_transaction.created,
        'issuing_transaction.updated': handler.issuing_transaction.updated,
        'mandate.updated': handler.mandate.updated,
        'order.created': handler.order.created,
        'order.payment_failed': handler.order.payment_failed,
        'order.payment_succeeded': handler.order.payment_succeeded,
        'order.updated': handler.order.updated,
        'order_return.created': handler.order_return.created,
        'payment_intent.amount_capturable_updated': handler.payment_intent.amount_capturable_updated,
        'payment_intent.canceled': handler.payment_intent.canceled,
        'payment_intent.created': handler.payment_intent.created,
        'payment_intent.payment_failed': handler.payment_intent.payment_failed,
        'payment_intent.processing': handler.payment_intent.processing,
        'payment_intent.requires_action': handler.payment_intent.requires_action,
        'payment_intent.succeeded': handler.payment_intent.succeeded,
        'payment_method.attached': handler.payment_method.attached,
        'payment_method.automatically_updated': handler.payment_method.automatically_updated,
        'payment_method.detached': handler.payment_method.detached,
        'payment_method.updated': handler.payment_method.updated,
        'payout.canceled': handler.payout.canceled,
        'payout.created': handler.payout.created,
        'payout.failed': handler.payout.failed,
        'payout.paid': handler.payout.paid,
        'payout.updated': handler.payout.updated,
        'person.created': handler.person.created,
        'person.deleted': handler.person.deleted,
        'person.updated': handler.person.updated,
        'plan.created': handler.plan.created,
        'plan.deleted': handler.plan.deleted,
        'plan.updated': handler.plan.updated,
        'price.created': handler.price.created,
        'price.deleted': handler.price.deleted,
        'price.updated': handler.price.updated,
        'product.created': handler.product.created,
        'product.deleted': handler.product.deleted,
        'product.updated': handler.product.updated,
        'promotion_code.created': handler.promotion_code.created,
        'promotion_code.updated': handler.promotion_code.updated,
        'quote.accepted': handler.quote.accepted,
        'quote.canceled': handler.quote.canceled,
        'quote.created': handler.quote.created,
        'quote.finalized': handler.quote.finalized,
        'radar.early_fraud_warning.created': handler.radar.early_fraud_warning.created,
        'radar.early_fraud_warning.updated': handler.radar.early_fraud_warning.updated,
        'recipient.created': handler.recipient.created,
        'recipient.deleted': handler.recipient.deleted,
        'recipient.updated': handler.recipient.updated,
        'reporting.report_run.failed': handler.reporting.report_run.failed,
        'reporting.report_run.succeeded': handler.reporting.report_run.succeeded,
        'reporting.report_type.updated': handler.reporting.report_type.updated,
        'review.closed': handler.review.closed,
        'review.opened': handler.review.opened,
        'setup_intent.canceled': handler.setup_intent.canceled,
        'setup_intent.created': handler.setup_intent.created,
        'setup_intent.requires_action': handler.setup_intent.requires_action,
        'setup_intent.setup_failed': handler.setup_intent.setup_failed,
        'setup_intent.succeeded': handler.setup_intent.succeeded,
        'sigma.scheduled_query_run.created': handler.sigma.scheduled_query_run.created,
        'sku.created': handler.sku.created,
        'sku.deleted': handler.sku.deleted,
        'sku.updated': handler.sku.updated,
        'source.canceled': handler.source.canceled,
        'source.chargeable': handler.source.chargeable,
        'source.failed': handler.source.failed,
        'source.mandate_notification': handler.source.mandate_notification,
        'source.refund_attributes_required': handler.source.refund_attributes_required,
        'source.transaction.created': handler.source.transaction.created,
        'source.transaction.updated': handler.source.transaction.updated,
        'transfer.created': handler.transfer.created,
        'transfer.failed': handler.transfer.failed,
        'transfer.paid': handler.transfer.paid,
        'transfer.reversed': handler.transfer.reversed,
        'transfer.updated': handler.transfer.updated,
    }

    # handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_price_id = session.get("membership")

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id = client_reference_id)
        UserMembership.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_price_id,
        )
        print(user.username + " just subscrbed.")

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
