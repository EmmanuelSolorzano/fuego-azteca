/** @odoo-module */

import { loadJS } from "@web/core/assets"
//import getDataset from "../getDataset"
const { Component, onWillStart, useRef, onMounted } = owl

export class StatusChart extends Component {
    setup(){
        this.chartRef = useRef("status_chart")
        onWillStart(async ()=>{
          await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js")
          const response = await fetch('/fn2', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ "data" : "marital"}),
          });
          // Handle the response here
          const data = await response.json();
          var objData = JSON.parse(data.result || "{}");
          this.labels = objData["label"] || [];
          this.dataChart = objData["data"] || [];
          //console.log(objData["Ganancias totales"]);
        })

        onMounted(()=>this.renderChart())
    }

    renderChart(){
        new Chart(this.chartRef.el,
        {
          type: this.props.type,
          data: {
            labels: this.labels,
            datasets: [{
              label: 'Personas',
              data: this.dataChart,
            }]
          },
          options: {
            responsive: true,
            plugins: {
              legend: {
                position: 'bottom',
              },
              title: {
                display: true,
                text: this.props.title,
                position: 'bottom',
              }
            }
          },
        }
      );
    }
}

StatusChart.template = "owl.StatusChart"