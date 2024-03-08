/** @odoo-module */

import { registry } from "@web/core/registry"
import { KpiCard } from "./kpi_card/kpi_card"
import { StateSalesChart } from "./state_sales_chart/state_sales_chart"
import { SKUSalesChart } from "./sku_sales_chart/sku_sales_chart"
import { AgeChart } from "./age_chart/age_chart"
import { StatusChart } from "./status_chart/status_chart"
import { loadJS } from "@web/core/assets"
const { Component, onWillStart, useRef, onMounted } = owl

export class OwlSalesDashboard extends Component {
    setup(){

    }
}

OwlSalesDashboard.template = "owl.OwlSalesDashboard"
OwlSalesDashboard.components = { KpiCard, StateSalesChart, SKUSalesChart, AgeChart, StatusChart }

registry.category("actions").add("owl.sales_dashboard", OwlSalesDashboard)