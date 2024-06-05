from rest_framework import serializers
from .models import Order, OrderLine

class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ['id', 'product_id', 'quantity', 'unit_price', 'total_price', 'created_at', 'updated_at']

class OrderSerializer(serializers.ModelSerializer):
    order_lines = OrderLineSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'customer', 'billing_address', 'shipping_address', 'created_at', 'updated_at', 'status', 'order_lines']

    def create(self, validated_data):
        order_lines_data = validated_data.pop('order_lines')
        order = Order.objects.create(**validated_data)
        for order_line_data in order_lines_data:
            OrderLine.objects.create(order=order, **order_line_data)
        return order
