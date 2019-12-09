// TODO: Probably a good idea to ping the server here and get the state of the RPi?
// or maybe we can pass that data into this form on page load

/*
 * Component switch for turning the RGB LED Matrix display on/off
 * Fairly strongly coupled with this main app
 */
Vue.component('switch-led', {
	data: function() {
		return { }
	},
	props: ['checked'],
	template: `
		<div>
			<label class="switch">
				<input type="checkbox" 
				 :checked="checked" 
				 @change="$emit('change', $event.target.checked)">
				<span class="slider"></span>
			</label>
		</div>
	`
})

Vue.component('open-image-file', {
	data: function() {
		return {
		}
	},
	props: {
		poweron: Boolean,
		url: String
	},
	methods: {
		openFile: function(event) {
			url = event.target.value;
		},
		submitFile: function() {
			//
		},
		submitURL: function() {
			//
		}
	},
	computed: {
		enabled: function() {
			return !this.poweron;
		}
	},
	template: `
		<form action="#" method="post">
			<div>
				<input type="text" 
				 v-model:value="url" 
				 placeholder="Enter an image or video URL">
				 <button 
				  type="submit" 
				  :disabled="enabled">
				  Submit
				 </button>
			</div>
			<div>
				<input 
				 type="file" 
				 name="openFileDialog"
				 :disabled="enabled"
				 @change="openFile($event)"/>
			</div>
		</form>
	`
})

Vue.component('current-image-thumbnail', {
	data: function() {
		return {
		}
	},
	props: ['src', 'alt', 'thumbstyle'],
	methods: {
		switchPower: function(newValue) {
			//
		}
	},
	template: `
		<div>
			<div>
				<h3>Now playing</h3>
			</div>
			<div>
				<button type="button"><</button>
				<img v-bind:src="src" v-bind:alt="alt" height="50" width="50"/>
				<button type="button">></button>
			</div>
		</div>
	`
})

var control_app = new Vue({
	el: '#control-app',
	data: {
		/* The true state of the RPi RGB LED Matrix display
		 * All other components should reference this for
		 * conditional rendering/computing */
		poweron: true,
		brightness: 50
	},
	watch: {
		/*
		poweron: function(val) {
			// TODO: May not need this, but for debugging this will help
			alert("poweron set to " + this.poweron);
		}
		*/
	}
})
